import os

from dotenv import load_dotenv
load_dotenv()

from web3 import Web3

from etherscan_py import etherscan_py
client = etherscan_py.Client(os.getenv("ETHERSCAN_API_KEY"))


def get_latest_block() -> int:
    """Gets the highest Ethereum block height."""
    return client.get_latest_block_height()

def is_address(address: str) -> bool:
    """Given a string, return True if a valid Ethereum address."""
    return Web3.isAddress(address)

def on_message(func: any) -> any:
    """When a message comes in, make sure chat_id is in whitelist."""
    whitelisted_group = [int(os.getenv("TELEGRAM_GROUP_CHAT_ID")), int(os.getenv("TELEGRAM_BOT_CHAT_ID"))]
    def is_whitelisted(*args, **kwargs):
        if args[0].message.chat_id in whitelisted_group:
            return func(args[0], args[1])
        else:
            print(args[0].message.chat_id, " not in whitelist!")
    return is_whitelisted