import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH")

bot = Client(
        ":ban:",
	API_HASH,
        API_ID,
	bot_token=BOT_TOKEN,
    )

@bot.on_message(filters.command('start'))
async def start(bot, message):
	text = 'Hey, I am Autoban Bot'
	await message.reply(text, quote=True)
	return

@bot.on_message(filters.new_chat_members)
async def kick(bot, new_chat_members):
	try:
	   await new_chat_members.kick()
	   return 
	except Expection as e
	print(e)

bot.start()	
bot.run()
