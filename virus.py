import telebot
import requests
from smdo import download
import os
from time import sleep
import time


token = os.environ.get("TOKEN")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def txt(message):
	idd = message.from_user.id
	bot.send_message(message.chat.id,"""-  بوت تحميل من جميع الموقع . 
- لتحميل فديو ارسل رابط المنشور .
- التحميل بدون علامة مائية او اي حقوق اخرى.""",reply_to_message_id=message.message_id)

@bot.message_handler(content_types=['text'])
def txt(message):
	idd = message.from_user.id
	if message.text.startswith('https://') or
	message.text.startswith('http://'):
		link = message.text
		msg = bot.reply_to(message,f"• يتم التحميل ..")
		smdo = download(
		url=link,
		format='1080',
		message='none')
		req = requests.get(f"{smdo}",allow_redirects=True)
		file = open('vid.mp4','wb')
		file.write(req.content)
		vid = open("vid.mp4","rb")
		bot.send_video(message.chat.id,vid,caption=f"• تم تحميل الفيديو.")
		os.remove("vid.mp4")
		bot.delete_message(message.chat.id,msg.message_id)
	else:
		pass
bot.infinity_polling()