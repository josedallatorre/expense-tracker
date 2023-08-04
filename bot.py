import os
from dotenv import load_dotenv
import telebot

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM-BOT-TOKEN')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()