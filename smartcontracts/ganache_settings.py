from utils.environment import env

ACCOUNT_ADDRESS = '0xd4b81eFe65F4d8D91e59fd343DF74A172fD32f9F'
ACCOUNT_PRIVATE_KEY = env('ACCOUNT_PRIVATE_KEY', '')

ACCOUNT_ADDRESS_2 = '0x3e0cAc50d20912a19e190E1B48854a9E7cEa5e34'
ACCOUNT_PRIVATE_KEY_2 = env('ACCOUNT_PRIVATE_KEY_2', '')

HOST_ADDRESS = 'HTTP://127.0.0.1:7545'

# Contracts info
CONTRACTS = {
    '01': {
        'address': '0x13866BEB43c13d347e62e1F2140445071587c6c0',
        'abi': [{"constant":True,"inputs":[{"name":"ots","type":"string"}],"name":"getHash","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"ots","type":"string"}],"name":"getBlockNumber","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"ots","type":"string"},{"name":"file_hash","type":"string"}],"name":"verify","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"selfDestroy","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"ots","type":"string"},{"name":"file_hash","type":"string"}],"name":"stamp","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":True,"name":"hash","type":"string"},{"indexed":True,"name":"ots","type":"string"}],"name":"Stamped","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"}],"name":"Deploy","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"}],"name":"SelfDestroy","type":"event"}],
    },
}

CONTRACT_VERSION = '01'

DEBUG = True

TEMPORARY_OTS_PREFIX = '0x'
PERMANENT_OTS_PREFIX = '1x'

