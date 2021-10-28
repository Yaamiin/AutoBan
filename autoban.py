import asyncio
from pyrogram import Client as Bot, filters, idle
from pyrogram.types import Message, User
from config import API_ID, API_HASH, BOT_TOKEN

bot = Bot(
    ':ban:',
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

@bot.on_message(filters.command('start'))
async def start(bot, message):
    text = 'Hey, I am Autoban Bot \n\n I Can Ban a Member After Joining The group. \n\n 📖 Note - Added Member will not be banned. \n\n ⚠️Warning- My use is for personal Groups.\n\n ©️ @Somalimusicbot'
    await message.reply(text, quote=True)
    return

@bot.on_message(filters.new_chat_members)
async def kick(bot, m: Message):
    try:
        await bot.kick_chat_member(m.chat.id, m.from_user.id)
        await asyncio.sleep(2)
        await unban.kick_chat_member(m.chat.id, m.from_user.id)
        return
    except Exception as e:
        print(e)

	
bot.start()
idle()
