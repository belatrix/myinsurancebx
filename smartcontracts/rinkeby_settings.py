from utils.environment import env

ACCOUNT_ADDRESS = '0x511844fCe794ad979C19067FF3dEf9647bdC8474'
ACCOUNT_PRIVATE_KEY = env('RINKEBY_PRIVATE_KEY', '')

HOST_ADDRESS = 'HTTP://127.0.0.1:8545'

# Contracts info
CONTRACTS = {
    '01': {
        'address': "0xbF15f0eBbfee5Acb1aFa8aFc0DD131d83d1964a2",
        'abi': '[{"constant":true,"inputs":[{"name":"ots","type":"string"}],"name":"getHash","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"ots","type":"string"}],"name":"getBlockNumber","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"ots","type":"string"},{"name":"file_hash","type":"string"}],"name":"verify","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"selfDestroy","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"ots","type":"string"},{"name":"file_hash","type":"string"}],"name":"stamp","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"hash","type":"string"},{"indexed":true,"name":"ots","type":"string"}],"name":"Stamped","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"}],"name":"Deploy","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"}],"name":"SelfDestroy","type":"event"}]',
    },
}

CONTRACT_VERSION = '01'

DEBUG = True

TEMPORARY_OTS_PREFIX = '0x'
PERMANENT_OTS_PREFIX = '1x'

