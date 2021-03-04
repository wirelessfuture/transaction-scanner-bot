from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from etherscan import get_transactions


def check_for_transactions() -> None:
    new_transactions = get_transactions()
    print(new_transactions)