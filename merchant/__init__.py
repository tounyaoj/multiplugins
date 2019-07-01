import logging
import os
import sys
from datetime import datetime
import asyncio
import concurrent.futures

import dotenv
from pyrogram import Client
from walrus import Walrus

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARN)
LOGS = logging.getLogger(__name__)


# Check for Python 3.6 or newer
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGS.error("You MUST use at least Python 3.6. Bot Quitting")
    quit(1)


dotenv.load_dotenv()


# Load variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_NAME = os.getenv("SESSION_NAME")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_DB = os.getenv("REDIS_DB")
MAXIMUM_WORKERS = int(os.getenv("MAXIMUM_WORKERS"))

# Load APIs
THECATAPI = os.getenv("THECATAPI")


# Setup client and redis
BOT = Client(session_name=SESSION_NAME, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
db = Walrus(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


# Setup executor
executor = concurrent.futures.ProcessPoolExecutor(max_workers=MAXIMUM_WORKERS)