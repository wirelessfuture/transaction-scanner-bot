from helpers import get_latest_block

from db import InMemoryDB
db = InMemoryDB(get_latest_block())