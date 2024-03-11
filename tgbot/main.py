import bot
from datetime import datetime
import db
import csv_reader
import numpy as np
from psycopg2.extensions import register_adapter, AsIs
register_adapter(np.int64, AsIs)

def init_bot():
    bot.send_welcome
init_bot()


