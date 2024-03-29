from datetime import datetime
import os
from pathlib import Path
import telebot
import db
import csv_reader
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
	t = message.text.split()
	user_id = message.from_user.id
	data= t[0]
	date_object = datetime.strptime(data, '%Y-%m-%d').date()
	a = t[1]
	if "€" in a:
		a = a.replace("€", "")
	descr = t[2]
	t1 = (date_object.isoformat(), a, descr, user_id)
	bot.reply_to(message, "Inserting with date: " + str(data)+ " amount " + str(a)+ " with description " + str(descr))
	cur, conn = db.connect()
	db.insert_transaction(cur, conn, t1)
	db.close(cur, conn)
	bot.reply_to(message, "Inserted correctly")


# Handles all text messages 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

# Handles all document, accept only csv file
@bot.message_handler(content_types=['document'])
def handle_document(message):
	if not message.document.file_name.endswith('.csv'):
		bot.reply_to(message, "Must be a csv file")
	else:
		bot.reply_to(message, "Saving the csv")
		file_name = message.document.file_name
		file_info = bot.get_file(message.document.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		with open('./' + file_name, 'wb') as new_file:
			new_file.write(downloaded_file)
		df = csv_reader.open_csv(file=file_name)
		df_cleaned = csv_reader.clean_df(df)
		n_rows = df_cleaned.__len__()
		for row in range(n_rows):
			t = csv_reader.row(df_cleaned,row)
			data= t[0]
			date_object = datetime.strptime(data, '%d/%m/%Y').date()
			a = t[1].item()
			descr = t[2]
			user_id = message.from_user.id
			print(type(date_object))
			print(date_object)  # printed in default format
			print(a, type(a))
			t1 = (date_object.isoformat(), a, descr, user_id)
			bot.reply_to(message, "Inserting with date: " + str(data)+ " amount " + str(a)+ " with description " + str(descr))
			cur, conn = db.connect()
			db.insert_transaction(cur, conn, t1)
			db.close(cur, conn)
			bot.reply_to(message, "Inserted correctly")

bot.infinity_polling()