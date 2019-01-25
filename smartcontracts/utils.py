import datetime
import hashlib
import time
from settings import WALLET_ADDRESS, CONTRACT_VERSION
from ethereum.abi import (decode_abi, normalize_name as normalize_abi_method_name, method_id as get_abi_method_id)
from ethereum.utils import encode_int, zpad, decode_hex


class Utils():
    @staticmethod
    def sha256_encode(string):
        return hashlib.sha256(string.encode('utf-8')).hexdigest()

    @staticmethod
    def datetime_from_timestamp(timestamp):
        return datetime.datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

    @staticmethod
    def get_ots_hash(file_hash):
        #El ots se genera con los hashes sha256 de (archivo original+timestamp+dirección de la cuenta) + versión del contrato
        return Utils.sha256_encode(str(file_hash + Utils.sha256_encode(str(int(time.time()))) + Utils.sha256_encode(WALLET_ADDRESS))) + CONTRACT_VERSION

    @staticmethod
    def decode_contract_call(contract_abi, call_data):
        call_data_bin = decode_hex(call_data)
        method_signature = call_data_bin[:4]
        for description in contract_abi:
            if description.get('type') != 'function':
                continue
            method_name = normalize_abi_method_name(description['name'])
            arg_types = [item['type'] for item in description['inputs']]
            method_id = get_abi_method_id(method_name, arg_types)
            if zpad(encode_int(method_id), 4) == method_signature:
                try:
                    args = decode_abi(arg_types, call_data_bin[4:])
                except AssertionError:
                    # Invalid args
                    continue
                return method_name, args
