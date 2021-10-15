from pyrogram import Client, filters
from pyrogram.types import Message, User
from config import API_ID, API_HASH, BOT_TOKEN

bot = Client(
        ":ban:",
	API_ID,
	API_HASH,
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
