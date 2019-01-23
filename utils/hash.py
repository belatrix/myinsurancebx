from requests import get as request_get
from eth_hash.auto import keccak


def keccak_hash_file_url(file_url):
    response = request_get(file_url)
    file = response.content
    raw_hash = keccak.new(file)
    return raw_hash.digest().hex()


def keccak_hash_file(file):
    raw_hash = keccak.new(file)
    return raw_hash.digest().hex()
