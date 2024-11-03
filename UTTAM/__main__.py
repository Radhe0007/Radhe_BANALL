import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
import threading

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
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER = os.getenv("OWNER")

# Pyrogram client
app_pyrogram = Client(
    "banall",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

@app_pyrogram.on_message(
    filters.command("start") & filters.private            
)
async def start_command(client, message: Message):
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

@app_pyrogram.on_message(
    filters.command("banall") & filters.group
)
async def banall_command(client, message: Message):
    print("Getting members from {}".format(message.chat.id))
    async for i in app_pyrogram.get_chat_members(message.chat.id):
        try:
            await app_pyrogram.ban_chat_member(chat_id=message.chat.id, user_id=i.user.id)
            print("Kicked {} from {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("Failed to kick {}: {}".format(i.user.id, e))
    print("Process completed")

# Function to run Flask app
def run_flask():
    app_flask.run(host="0.0.0.0", port=8000)

# Function to run Pyrogram bot
def run_pyrogram():
    app_pyrogram.start()
    print("Banall-Bot Booted Successfully")
    idle()

# Running Flask app in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Running Pyrogram bot
run_pyrogram()
