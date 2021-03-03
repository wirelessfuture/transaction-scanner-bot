from typing import List

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from validators import is_address
from entities import Address

from db import InMemoryDB
db = InMemoryDB()

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Inform users how to use the bot."""
    update.message.reply_text(
        'Use /add <address> <name> to add to watchlist\n' \
        'Use /remove <name> to remove from watchlist\n' \
        'Use /watchlist to see the current watchlist'
    )

def add_address(update: Update, context: CallbackContext) -> None:
    """Add an address to the watchlist."""
    try:
        address = str(context.args[0]) # args[0] should contain the address
        name = str(context.args[1]) # args[1] should contain the name
        if not is_address(address):
            update.message.reply_text('Sorry, that address looks weird!')
            return

        db.add_address(Address(name=name, address=address))
        update.message.reply_text(f'OK! I have added {address} to the watchlist!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /add <address> <name>')

def remove_address(update: Update, context: CallbackContext) -> None:
    """Remove the address if the user changed their mind."""
    try:
        name = str(context.args[0])
        db.remove_address(name)
        update.message.reply_text(f'OK! I have removed {name} from the watchlist!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /remove <name>')

def get_address_list(update: Update, context: CallbackContext) -> None:
    """Returns the current addresslist to the user."""
    addresses = db.get_addresses()
    if len(addresses) > 0:
        pass