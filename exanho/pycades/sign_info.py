import base64
import datetime
import logging
import pycades
import re

from .utilities import build_hashed_data

logger = logging.getLogger(__name__)
    
AVAILABLE_HASH_ALGORITHM_DICT = {
    100:pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256,
    101:pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256,
    102:pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256,
    110:pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_HMAC,
    111:pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256,
    112:pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256
}

AVAILABLE_ENCODE_DICT = {
    'BASE64':pycades.CAPICOM_ENCODE_BASE64,
    'BINARY':pycades.CADESCOM_BASE64_TO_BINARY,
    'ANY':pycades.CAPICOM_ENCODE_ANY
}

def by_content_sign(content:str, sign:str, encoding_type:str):
    signed_data = pycades.SignedData()
    signed_data.ContentEncoding = AVAILABLE_ENCODE_DICT[encoding_type]
    signed_data.Content = base64.b64encode(content.encode()).decode("utf-8")

    try:
        signed_data.VerifyCades(sign, pycades.CADESCOM_CADES_BES, True) # True - because the content and signature are separate
    except Exception as ex:
        logger.exception(ex)
        raise

    return _check_and_fill(dict(), signed_data)

def by_file_hash_sign(_file:bytes, sign:str, hash_alg:int):
    hashed_data = build_hashed_data(_file, AVAILABLE_HASH_ALGORITHM_DICT[hash_alg])

    signed_data = pycades.SignedData()

    try:
        signed_data.VerifyHash(hashed_data, sign, pycades.CADESCOM_CADES_BES)
    except Exception as ex:
        logger.exception(ex)
        raise

    return _check_and_fill(dict(), signed_data)

def by_hash_sign(hash:str, sign:str, hash_alg:int):
    hashed_data = pycades.HashedData()
    hashed_data.Algorithm = AVAILABLE_HASH_ALGORITHM_DICT[hash_alg]
    hashed_data.DataEncoding = pycades.CADESCOM_BASE64_TO_BINARY
    hashed_data.SetHashValue(hash)

    signed_data = pycades.SignedData()
    try:
        signed_data.VerifyHash(hashed_data, sign, pycades.CADESCOM_CADES_BES)
    except Exception as ex:
        logger.exception(ex)
        raise

    return _check_and_fill(dict(), signed_data)
    
def _check_and_fill(dto:dict, signed_data):

    if signed_data.Signers.Count > 1:
        raise Exception('Содержимое содержит несколько ЭП')

    signer = signed_data.Signers.Item(1) # TODO: We assume that there is one signer
    dto = _check_cert(dto, signer)
    dto = _fill_cert_info(dto, signer.Certificate)

    return dto


def _check_cert(dto, signer):
    signature_status = signer.SignatureStatus.IsValid
    if not signature_status:
        raise Exception(f'Статус электронной подписи: {signature_status}')

    is_valid = signer.Certificate.IsValid().Result
    if not signature_status or not is_valid:
        raise Exception('Ошибка при проверке цепочки сертификатов') # Возможно на сервере не установлены сертификаты УЦ, выдавшего сертификат

    algorithm = signer.Certificate.PublicKey().Algorithm
    _algorithm_oid = algorithm.Value
    if _algorithm_oid not in ('1.2.643.7.1.1.1.1', '1.2.643.7.1.1.1.2'):
        raise Exception(f'Принимается только алгоритм подписи ГОСТ Р 34.10-2012 с ключом 256 бит или 512 бит (Вы используете {algorithm.FriendlyName})')

    dto['algorithm_oid'] = _algorithm_oid
    return dto

def _fill_cert_info(dto:dict, cert):
    _certificate = cert.Export(pycades.CAPICOM_ENCODE_BINARY)

    dto['thumbprint'] = cert.Thumbprint.upper()
    dto['serial_number'] = cert.SerialNumber.upper()
    dto['valid_from'] = datetime.datetime.strptime(cert.ValidFromDate, '%d.%m.%Y %H:%M:%S')
    dto['valid_to'] = datetime.datetime.strptime(cert.ValidToDate, '%d.%m.%Y %H:%M:%S')
    dto['version'] = cert.Version

    dto['issuer_name'] = cert.IssuerName
    parsed_issuer_name_pairs = _parse_common_cert_property(cert.IssuerName)
    dto['issuer_name_CN'] = parsed_issuer_name_pairs.get('CN', None)
    dto['issuer_name_O'] = parsed_issuer_name_pairs.get('O', None)
    dto['issuer_name_OU'] = parsed_issuer_name_pairs.get('OU', None)
    dto['issuer_name_L'] = parsed_issuer_name_pairs.get('L', None)
    dto['issuer_name_S'] = parsed_issuer_name_pairs.get('S', None)
    dto['issuer_name_C'] = parsed_issuer_name_pairs.get('C', None)

    dto['subject_name'] = cert.SubjectName
    parsed_subject_name_pairs = _parse_common_cert_property(cert.SubjectName)
    dto['subject_name_SN'] = parsed_subject_name_pairs.get('SN', None)
    dto['subject_name_G'] = parsed_subject_name_pairs.get('G', None)
    dto['subject_name_T'] = parsed_subject_name_pairs.get('T', '')
    dto['subject_name_CN'] = parsed_subject_name_pairs.get('CN', None)
    dto['subject_name_OU'] = parsed_subject_name_pairs.get('OU', None)
    dto['subject_name_O'] = parsed_subject_name_pairs.get('O', None)
    dto['subject_name_L'] = parsed_subject_name_pairs.get('L', None)
    dto['subject_name_S'] = parsed_subject_name_pairs.get('S', None)
    dto['subject_name_C'] = parsed_subject_name_pairs.get('C', None)
    dto['subject_name_E'] = parsed_subject_name_pairs.get('E', None)

    _inn = parsed_subject_name_pairs.get('INN', None)
    if not _inn: _inn = parsed_subject_name_pairs.get('ИНН', None)
    if not _inn: _inn = parsed_subject_name_pairs.get('OID.1.2.643.3.131.1.1', None)

    _innle = parsed_subject_name_pairs.get('INNLE', None)
    if not _innle: _innle = parsed_subject_name_pairs.get('ИНН ЮЛ', None)
    if not _innle: _innle = parsed_subject_name_pairs.get('OID.1.2.643.100.4', None)
    if not _innle: _innle = parsed_subject_name_pairs.get('1.2.643.100.4', None)
    if _innle and _innle.startswith('#'): _innle = ''.join(char for char in bytes.fromhex(_innle[1:]).decode('utf-8') if char.isdigit())

    _kpp = parsed_subject_name_pairs.get('KPP', None)
    if not _kpp: _kpp = parsed_subject_name_pairs.get('КПП', None)
    if not _kpp: _kpp = parsed_subject_name_pairs.get('OID.1.2.643.3.61.502710.1.7', None)

    _ogrn = parsed_subject_name_pairs.get('OGRN', None)
    if not _ogrn: _ogrn = parsed_subject_name_pairs.get('ОГРН', None)
    if not _ogrn: _ogrn = parsed_subject_name_pairs.get('OID.1.2.643.100.1', None)

    _ogrnip = parsed_subject_name_pairs.get('OGRNIP', None)
    if not _ogrnip: _ogrnip = parsed_subject_name_pairs.get('ОГРНИП', None)
    if not _ogrnip: _ogrnip = parsed_subject_name_pairs.get('OID.1.2.643.100.5', None)

    _snils = parsed_subject_name_pairs.get('SNILS', None)
    if not _snils: _snils = parsed_subject_name_pairs.get('СНИЛС', None)
    if not _snils: _snils = parsed_subject_name_pairs.get('OID.1.2.643.100.3', None)

    # if ('UnstructuredName' in parsed_subject_name_pairs) or ('OID.1.2.840.113549.1.9.2' in parsed_subject_name_pairs) or ('UN' in parsed_subject_name_pairs):
    #     unstr_name = parsed_subject_name_pairs.get('UnstructuredName', parsed_subject_name_pairs.get('OID.1.2.840.113549.1.9.2', parsed_subject_name_pairs.get('UN', None)))
    for un_name in ('UnstructuredName', 'OID.1.2.840.113549.1.9.2', 'UN'):
        un_value = parsed_subject_name_pairs.get(un_name, None)
        if un_value:
            un_inn, un_kpp, un_ogrn = _parse_unstructured_name(un_value)
            if un_inn and not _inn: _inn = un_inn
            if un_kpp and not _kpp: _kpp = un_kpp
            if un_ogrn and not _ogrn: _ogrn = un_ogrn

    dto['inn'] = _inn
    dto['innle'] = _innle
    dto['kpp'] = _kpp
    dto['ogrn'] = _ogrn
    dto['ogrnip'] = _ogrnip
    dto['snils'] = _snils

    return dto

def _parse_common_cert_property(common_cert_property) -> dict:
    pairs = dict()

    compile_pattern = re.compile(r'\s*(?P<name>[^"=]+)\s*[=]\s*(?P<quoted>["])?(?(quoted)(?P<val_>([^"]|["]["])+)["]|(?P<val>([^,])+))\s*')
    for part_property in re.split(r',', common_cert_property):
        m = compile_pattern.search(part_property)
        if m:
            p_name = m.group('name')
            p_value = m.group('val') if m.group('val') else m.group('val_')
            if p_name and p_name not in pairs:
                if type(p_value) == str:
                    p_value = p_value.replace('""', '"')
                pairs[p_name] = p_value

    return pairs

def _parse_unstructured_name(unstructured_name:str):
    if not unstructured_name:
        return None, None, None

    un_inn = un_kpp = un_ogrn = None
    for un_part in re.split(r'\/', unstructured_name):
        compile_pattern = re.compile(r'\s*(?P<name>[^=]+)\s*[=]\s*(?P<val>\d+)')
        m = compile_pattern.search(un_part)
        if m:
            p_name = m.group('name')
            p_value = m.group('val')
            if p_name in ('INN', 'ИНН'): un_inn = p_value
            if p_name in ('KPP', 'КПП'): un_kpp = p_value
            if p_name in ('OGRN', 'ОГРН'): un_ogrn = p_value

    return un_inn, un_kpp, un_ogrn