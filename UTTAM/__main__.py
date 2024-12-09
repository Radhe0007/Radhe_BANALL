import os
import logging
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
import threading
import asyncio

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
    await app_pyrogram.send_message(
        chat_id=LOGGER_GROUP_ID,
        text=f"**Bot Started**\n\n"
             f"**Name:** [{bot.first_name}](tg://user?id={bot.id})\n"
             f"**ID:** `{bot.id}`\n"
             f"**Username:** @{bot.username}"
    )

# बॉट के कमांड हैंडलर्स
@app_pyrogram.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    user_mention = message.from_user.mention  # यूजर का मेंशन नाम प्राप्त करें
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
    # लॉगर ग्रुप में मैसेज भेजें
    try:
        await client.send_message(
            chat_id=LOGGER_GROUP_ID,
            text=f"{user_mention} just started the bot!"
        )
        logging.info("Logger message sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send logger message: {e}")

@app_pyrogram.on_message(filters.command("banall") & filters.group)
async def banall_command(client, message: Message):
    print("Getting members from {}".format(message.chat.id))
    async for i in app_pyrogram.get_chat_members(message.chat.id):
        try:
            await app_pyrogram.ban_chat_member(chat_id=message.chat.id, user_id=i.user.id)
            print("Kicked {} from {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("Failed to kick {}: {}".format(i.user.id, e))
    print("Process completed")

# Flask और Pyrogram बॉट रन करना
def run_flask():
    app_flask.run(host="0.0.0.0", port=8000)

async def run_pyrogram():
    await app_pyrogram.start()
    print("Banall-Bot Booted Successfully")
    await send_startup_message()  # बॉट स्टार्ट मैसेज भेजें
    await idle()

# Flask थ्रेड में चलाएं
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Main entry point for async Pyrogram bot
if __name__ == "__main__":
    asyncio.run(run_pyrogram())
