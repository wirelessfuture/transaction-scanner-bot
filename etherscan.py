import os

from typing import List

from dotenv import load_dotenv
load_dotenv()

from etherscan_py import etherscan_py
client = etherscan_py.Client(os.getenv("ETHERSCAN_API_KEY"))

from entities import Transaction


def get_transactions(from_block: int) -> List[Transaction]:
    """Given the wallet address, get all the latest transactions."""
    address = os.getenv("TARGET_ADDRESS")
    to_block = 'latest'
    transactions = client.get_all_transactions(
        from_address=address,
        status=2, 
        from_block=from_block, 
        to_block=to_block, 
        thread_count=1
    )
    transaction_list = []
    for tx in transactions:
        transaction_list.append(vars(tx))

    return transaction_list

def get_latest_block() -> int:
    return client.get_latest_block_height()