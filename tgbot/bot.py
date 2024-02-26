from datetime import datetime
import os
from pathlib import Path
import telebot
import db
from dotenv import load_dotenv
dotenv_path= Path('../.env')
load_dotenv(dotenv_path=dotenv_path)
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	user_id = message.from_user.id
	user_name = message.from_user.first_name
	user_last_name = message.from_user.last_name
	user_username = message.from_user.username
	print(user_id, user_name, user_last_name, user_username)
	t1 = (user_id, user_username)
	cur, conn = db.connect()
	db.insert_client(cur, conn, t1)
	db.close(cur, conn)

# Handles all text messages that match the regular expression for yyyy-mm-dd
@bot.message_handler(regexp="(\d{4})-(\d{2})-(\d{2})")
def handle_message(message):
	bot.reply_to(message, "ho trovato una data")
	t = message.text.split()
	user_id = message.from_user.id
	data= t[0]
	date_object = datetime.strptime(data, '%Y-%m-%d').date()
	a = t[1]
	descr = t[2]
	t1 = (date_object.isoformat(), a, descr, user_id)
	cur, conn = db.connect()
	db.insert_transaction(cur, conn, t1)
	db.close(cur, conn)

# Handles all text messages 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()