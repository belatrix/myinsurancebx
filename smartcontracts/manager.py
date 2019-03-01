from .ganache_settings import CONTRACTS, CONTRACT_VERSION, ACCOUNT_ADDRESS, HOST_ADDRESS

from django.db import models
from web3 import Web3, HTTPProvider
from web3.exceptions import CannotHandleRequest, UnhandledRequest
from web3.middleware import geth_poa_middleware


class ContractManager(models.Manager):

    @staticmethod
    def get_provider():

        try:

            web3 = Web3(HTTPProvider(HOST_ADDRESS))
            web3.middleware_stack.inject(geth_poa_middleware, layer=0)

            if not web3.isConnected():
                raise CannotHandleRequest
            
            return web3
        except UnhandledRequest:
            raise

    @staticmethod
    def get_current_contract():

        return ContractManager.get_contract(CONTRACT_VERSION)

    @staticmethod
    def get_contract(contract_version):
        
        web3 = ContractManager.get_provider()
        
        return web3.eth.contract(abi=CONTRACTS[contract_version]['abi'], address=Web3.toChecksumAddress(CONTRACTS[contract_version]['address']))

    @staticmethod
    def get_block(block_number):

        web3 = ContractManager.get_provider()
        return web3.eth.getBlock(block_number)

    @staticmethod
    def get_transaction(tx_hash):

        web3 = ContractManager.get_provider()
        return web3.eth.getTransaction(tx_hash)

    @staticmethod
    def stamp(ots_hash, file_hash):
        
        contract = ContractManager.get_current_contract()

        return contract.functions.stamp(ots_hash, file_hash).transact({'from': Web3.toChecksumAddress(ACCOUNT_ADDRESS)})

    @staticmethod
    def verify(contract_version, ots_hash, file_hash):
        contract = ContractManager.get_contract(contract_version)
        return contract.functions.verify(ots_hash, file_hash).call()

    @staticmethod
    def get_block_number(contract_version, ots_hash):
        contract = ContractManager.get_contract(contract_version)
        return contract.functions.getBlockNumber(ots_hash).call()
