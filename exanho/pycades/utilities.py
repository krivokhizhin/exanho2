import base64

import pycades

def build_hashed_data(data:bytes, algorithm=pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_512):
    data_b64str = base64.b64encode(data).decode(encoding="utf-8", errors="strict")

    hashed_data = pycades.HashedData()
    hashed_data.Algorithm = algorithm
    hashed_data.DataEncoding = pycades.CADESCOM_BASE64_TO_BINARY
    hashed_data.Hash(data_b64str)

    return hashed_data


def _compute_hash(data:bytes, algorithm=pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_512):
    hashed_data = build_hashed_data(data, algorithm)
    return hashed_data.Value

def hash_gost_2012_512(data:bytes):
    return _compute_hash(data, pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_512)

def hash_gost_2012_256(data:bytes):
    return _compute_hash(data, pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256)

def hash_gost_3411(data:bytes):
    return _compute_hash(data, pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411)