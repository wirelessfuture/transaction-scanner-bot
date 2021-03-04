import os

from typing import List, Dict

from dotenv import load_dotenv
load_dotenv()

from etherscan_py import etherscan_py
client = etherscan_py.Client(os.getenv("ETHERSCAN_API_KEY"))

from init_db import db
from entities import Transaction
from helpers import get_latest_block


def get_transactions() -> Dict[str, List[Transaction]]:
    """Check all addresses in db, get all the latest transactions."""

    # Iterate through address entities and get tx's from etherscan
    addresses = db.get_addresses()
    transaction_dict = dict()
    for address in addresses:
        address_to_get_tx = address.address
        from_block = db.last_block
        to_block = 'latest'
        transactions = client.get_all_transactions(
            from_address=address_to_get_tx,
            status=2, 
            from_block=from_block, 
            to_block=to_block, 
            thread_count=1
        )
        transaction_dict[address_to_get_tx] = list()
        for tx in transactions:
            transaction_dict[address_to_get_tx].append(Transaction(**vars(tx)))

    # Set the last block
    db.last_block = get_latest_block()

    return transaction_dict

