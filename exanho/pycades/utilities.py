import base64

import pycades

AVAILABLE_HASH_ALGORITHM_DICT = {
    100:pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411,
    101:pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256,
    102:pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_512,
    110:pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_HMAC,
    111:pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256_HMAC,
    112:pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_512_HMAC
}

AVAILABLE_ENCODE_DICT = {
    'BASE64':pycades.CAPICOM_ENCODE_BASE64,
    'BINARY':pycades.CADESCOM_BASE64_TO_BINARY,
    'ANY':pycades.CAPICOM_ENCODE_ANY
}

def build_hashed_data(data:bytes, algorithm=pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256):
    data_b64str = base64.b64encode(data).decode(encoding="utf-8", errors="strict")

    hashed_data = pycades.HashedData()
    hashed_data.Algorithm = algorithm
    hashed_data.DataEncoding = pycades.CADESCOM_BASE64_TO_BINARY
    hashed_data.Hash(data_b64str)

    return hashed_data


def _compute_hash(data:bytes, algorithm=pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256):
    hashed_data = build_hashed_data(data, algorithm)
    return hashed_data.Value

def hash_gost_2012_512(data:bytes):
    return _compute_hash(data, pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_512)

def hash_gost_2012_256(data:bytes):
    return _compute_hash(data, pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256)

def hash_gost_3411(data:bytes):
    return _compute_hash(data, pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411)

def _get_signer(thumbprint:str) -> pycades.Certificate:
    
    store = pycades.Store()
    store.Open(pycades.CADESCOM_CONTAINER_STORE, pycades.CAPICOM_MY_STORE, pycades.CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED)
    certs = store.Certificates
    for i in range(certs.Count):
        cert = certs.Item(i+1)
        if cert.Thumbprint == thumbprint and cert.PrivateKey is not None:
            signer = pycades.Signer()
            signer.Certificate = cert
            signer.CheckCertificate = True
            return signer

    return None

def sign(content:str, thumbprint:str, encoding_type:str, detached:bool):

    signer = _get_signer(thumbprint)
    if signer is None:
        raise Exception(f'Сертификат закрытого ключа с отпечатком {thumbprint} в хранилище не найден')
    
    signed_data = pycades.SignedData()
    signed_data.ContentEncoding = AVAILABLE_ENCODE_DICT[encoding_type]
    signed_data.Content = base64.b64encode(content.encode()).decode("utf-8")
    signature = signed_data.SignCades(signer, pycades.CADESCOM_CADES_BES, detached, pycades.CAPICOM_ENCODE_BASE64)

    return signature


def sign_hash(hash:str, thumbprint:str, hash_alg:int):

    signer = _get_signer(thumbprint)
    if signer is None:
        raise Exception(f'Сертификат закрытого ключа с отпечатком {thumbprint} в хранилище не найден')
    
    hashed_data = pycades.HashedData()
    hashed_data.Algorithm = AVAILABLE_HASH_ALGORITHM_DICT[hash_alg]
    hashed_data.DataEncoding = pycades.CADESCOM_BASE64_TO_BINARY
    hashed_data.SetHashValue(hash)

    signed_data = pycades.SignedData()
    signature = signed_data.SignHash(hashed_data, signer, pycades.CADESCOM_CADES_BES, pycades.CAPICOM_ENCODE_BASE64)

    return signature
