# from .ganache_settings import CONTRACTS, CONTRACT_VERSION, ACCOUNT_ADDRESS, HOST_ADDRESS
from .rinkeby_settings import CONTRACTS, CONTRACT_VERSION, ACCOUNT_ADDRESS, HOST_ADDRESS

from django.db import models
from web3 import Web3, HTTPProvider
from web3.exceptions import CannotHandleRequest, UnhandledRequest
from web3.middleware import geth_poa_middleware


class ContractManager(models.Manager):

    @staticmethod
    def get_provider():
        print('4- getting provider')
        try:
            web3 = Web3(HTTPProvider(HOST_ADDRESS))
            print('web3 provider is ', web3)
            web3.middleware_stack.inject(geth_poa_middleware, layer=0)  # setting proof of authority consensus
            print('setting PoA consensus successful')
            if not web3.isConnected():
                print('web3 not connected')
                raise CannotHandleRequest
            
            return web3
        except UnhandledRequest:
            print('failed getting provider from host ', HOST_ADDRESS)
            raise

    @staticmethod
    def get_current_contract():
        print('2- getting current contract')
        return ContractManager.get_contract(CONTRACT_VERSION)

    @staticmethod
    def get_contract(contract_version):
        print('3- getting contract version ', contract_version)
        web3 = ContractManager.get_provider()
        print('obtaining contract at address ', Web3.toChecksumAddress(CONTRACTS[contract_version]['address']))
        print('obtaining contract with abi ', CONTRACTS[contract_version]['abi'])
        return web3.eth.contract(abi=CONTRACTS[contract_version]['abi'], address=Web3.toChecksumAddress(CONTRACTS[contract_version]['address']))

    @staticmethod
    def get_block(block_number):
        print('getting block ', block_number)
        web3 = ContractManager.get_provider()
        return web3.eth.getBlock(block_number)

    @staticmethod
    def get_transaction(tx_hash):
        print('getting transaction ', tx_hash)
        web3 = ContractManager.get_provider()
        return web3.eth.getTransaction(tx_hash)

    @staticmethod
    def stamp(ots_hash, file_hash):
        print('1- stamping in blockchain')
        contract = ContractManager.get_current_contract()
        print('contract retreived successfully', contract)
        print('stamping with ots_hash', ots_hash)
        print('and file_hash', file_hash)
        print('from account address', Web3.toChecksumAddress(ACCOUNT_ADDRESS))
        return contract.functions.stamp(ots_hash, file_hash).transact({'from': Web3.toChecksumAddress(ACCOUNT_ADDRESS)})

    @staticmethod
    def verify(contract_version, ots_hash, file_hash):
        print("verificando con contrato version ", contract_version)
        print("ots_hash ", ots_hash)
        print("file_hash ", file_hash)
        contract = ContractManager.get_contract(contract_version)
        return contract.functions.verify(ots_hash, file_hash).call()

    @staticmethod
    def get_block_number(contract_version, ots_hash):
        print('getting block number')
        print('with contract version ', contract_version)
        print('from ots_hash ', ots_hash)
        contract = ContractManager.get_contract(contract_version)
        return contract.functions.getBlockNumber(ots_hash).call()
