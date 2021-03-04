import os
import logging
import time

import schedule

from telegram.ext import Updater, CommandHandler

from dotenv import load_dotenv
load_dotenv()

from commands import (
    start,
    add_address,
    remove_address,
    get_address_list
)

from worker import check_for_transactions

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.getenv("TELEGRAM_BOT_TOKEN"))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))
    dispatcher.add_handler(CommandHandler("add", add_address))
    dispatcher.add_handler(CommandHandler("remove", remove_address))
    dispatcher.add_handler(CommandHandler("watchlist", get_address_list))

    # Start the Bot
    updater.start_polling()

    # Schedule the worker task
    schedule.every(2).minutes.do(check_for_transactions)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()