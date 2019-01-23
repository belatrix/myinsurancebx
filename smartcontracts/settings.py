from utils.environment import env

CONTRACT_ADDRESS = ''

WALLET_ADDRESS = env('WALLET_ADDRESS')
WALLET_PRIVATE_KEY = env('WALLET_PRIVATE_KEY')

HOST_ADDRESS = env('HOST_ADDRESS')

#Contracts info
CONTRACTS = {
    '01':{
        'address': '',
        'abi': [],
    },
}

CONTRACT_VERSION = '01'

DEBUG = False

TEMPORARY_PREFIX = '0x'
PERMANENT_PREFIX = '1x'

