import os
import time
from datetime import datetime

from typing import Dict, List

from dotenv import load_dotenv
load_dotenv()

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

from etherscan import get_transactions
from entities import Transaction
from init_db import db


def check_for_transactions() -> Dict[str, List[Transaction]]:
    """Get's the recent successful transactions."""
    transactions = get_transactions()
    if transactions != None:
        return transactions

def parse_transactions(transactions: Dict[str, List[Transaction]]) -> List[str]:
    """Parses the transactions into separate messages."""
    keys_for_message = [
        "txhash",
        "timestamp"
    ]
    
    messages = []
    for address in transactions:
        address_name = db.get_name_by_address(address)
        for tx in transactions[address]:
            tx_data = []
            for key, value in vars(tx).items():
                if key in keys_for_message:
                    if key == "txhash":
                        tx_data.append(f'{key.upper()}: https://etherscan.io/tx/{value}\n')
                    if key == "timestamp":
                        tx_data.append(f'{key.upper()}: {datetime.utcfromtimestamp(int(value)).strftime("%H:%M:%S")}\n')
            tx_data.insert(0, f'{address_name.upper()}\n')
            messages.append(''.join(tx_data))

    return messages
    
def send_bot_message(message: str) -> None:
    """Given the message, have the bot send it in."""
    channel_id = int(os.getenv("TELEGRAM_GROUP_CHAT_ID"))
    bot = Bot(os.getenv("TELEGRAM_BOT_TOKEN"))
    bot.send_message(channel_id, message)

def worker() -> None:
    """Main worker that Gets tx, parses them, and sends the messages."""
    new_transactions = get_transactions()
    parsed_messages = parse_transactions(new_transactions)
    for message in parsed_messages:
        send_bot_message(message)
        time.sleep(2)