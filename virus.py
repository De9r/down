from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio,os,smdo
from smdo import download
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
token = os.environ.get("TOKEN")
app = Client("tag", bot_token=token, api_id = api_id, api_hash = api_hash)

async def is_Admin(chat,id):
	admins = []
	sync for m in app.get_chat_members(chat, filter=enums.ChatMembersFilter.ADMINISTRATORS):
		admins.append(m.user.id)
	if id in admins :
		return True
	else :
		return False 

@app.on_message(filters.command(["start"]))
async def everyone(client, message):
	await message.reply("""-  بوت تحميل من جميع الموقع . 
- لتحميل فديو ارسل رابط المنشور .
- التحميل بدون علامة مائية او اي حقوق اخرى.""")

@bot.on_message(filters.text) #يقرة كل الرسائل
async def text(bot,message):
	start_text = message.text.startswith
	reply = message.reply_text #يرد عالرسالة
	mention = message.from_user.mention
	if start_text("http"):
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
	else:
		pass	

app.run()