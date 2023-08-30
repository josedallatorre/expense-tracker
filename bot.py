import os
import telebot


TELEGRAM_BOT_TOKEN = "609830348:AAFWFZ6_JF69LeUxrdgkg3POm3u2-dK7v4o"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()