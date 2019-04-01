from utils.environment import env

ACCOUNT_ADDRESS = '0x511844fCe794ad979C19067FF3dEf9647bdC8474'
ACCOUNT_PRIVATE_KEY = env('RINKEBY_PRIVATE_KEY', '')

HOST_ADDRESS = 'HTTP://127.0.0.1:8545'

# Contracts info
CONTRACTS = {
    '01': {
        'address': '0xbF15f0eBbfee5Acb1aFa8aFc0DD131d83d1964a2',
        'abi': [[{"constant":True,"inputs":[{"name":"ots","type":"string"}],"name":"getHash","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"ots","type":"string"}],"name":"getBlockNumber","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"ots","type":"string"},{"name":"file_hash","type":"string"}],"name":"verify","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"selfDestroy","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"ots","type":"string"},{"name":"file_hash","type":"string"}],"name":"stamp","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":True,"name":"hash","type":"string"},{"indexed":True,"name":"ots","type":"string"}],"name":"Stamped","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"}],"name":"Deploy","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"}],"name":"SelfDestroy","type":"event"}]],
    },
}

CONTRACT_VERSION = '01'

DEBUG = True

TEMPORARY_OTS_PREFIX = '0x'
PERMANENT_OTS_PREFIX = '1x'

