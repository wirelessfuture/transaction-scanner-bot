from web3 import Web3

def is_address(address: str) -> bool:
    """Given a string, return True if a valid Ethereum address."""
    return Web3.isAddress(address)