import os
import time

from typing import List, Dict, Union

from dotenv import load_dotenv
load_dotenv()

from etherscan_py import etherscan_py
client = etherscan_py.Client(os.getenv("ETHERSCAN_API_KEY"))

from init_db import db
from entities import Transaction
from helpers import get_latest_block


def get_transactions() -> Union[Dict[str, List[Transaction]], None]:
    """Check all addresses in db, get all the latest transactions."""
    # Iterate through address entities and get tx's from etherscan
    addresses = db.get_addresses()
    transaction_dict = {}
    for address in addresses:
        address_to_get_tx = address.address
        from_block = db.last_block
        to_block = 'latest'
        transactions = client.get_all_transactions(
            from_address=address_to_get_tx,
            status=1, 
            from_block=from_block, 
            to_block=to_block, 
            thread_count=1
        )
        if transactions != None:
            transaction_dict[address_to_get_tx] = []
            for tx in transactions:
                transaction_dict[address_to_get_tx].append(Transaction(**vars(tx)))
        else:
            return None # Return None if no tx are found
        time.sleep(2)

    # Set the last block
    db.last_block = get_latest_block()

    return transaction_dict