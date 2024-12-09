import os
import logging
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired
from datetime import datetime
import pytz

# Logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Config vars (Use environment variables if running on server)
API_ID = int(os.getenv("API_ID", "16457832"))
API_HASH = os.getenv("API_HASH", "3030874d0befdb5d05597deacc3e83ab"))
BOT_TOKEN = os.getenv("BOT_TOKEN", "7538146982:AAGeiAfuNVs-gEK1gfOHcPuwbv_5JCv2nvo")
LOGGER_GROUP_ID = int(os.getenv("LOGGER_GROUP_ID", "-1002043570167"))  # Log group ID
OWNER = os.getenv("OWNER", "BABY09_WORLD")

# Pyrogram client initialization
app = Client(
    "banall",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Function to get current time in IST (Indian Standard Time)
def get_indian_time():
    tz = pytz.timezone("Asia/Kolkata")
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    user_mention = message.from_user.mention  # Get the user's mention
    user_id = message.from_user.id            # Get the user's ID
    user_username = message.from_user.username if message.from_user.username else "No Username"  # Get the username, or 'No Username' if not available

    # Send a reply message to the user
    await message.reply_photo(
        photo="https://telegra.ph/file/62e2e9fc93cd51219264f.jpg",
        caption=f"╭───────────────────⦿\n│❍ • ʜᴇʏ ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ ʙᴀɴ •\n│❍ • ᴀʟʟ ʙᴏᴛ ᴡʜɪᴄʜ ɪs ʙᴀsᴇᴅ ᴏɴ •\n│• ᴘʏʀᴏɢʀᴀᴍ •\n│❍ • ʟɪʙʀᴀʀʏ ᴛᴏ ʙᴀɴ ᴏʀ ᴅᴇsᴛʀᴏʏ •\n│❍ • ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ᴀ ɢʀᴘ •\n│• ᴡɪᴛʜ ɪɴ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs •\n│❍ • ɴᴏ sᴛᴏᴘ + ɴᴏ ʟᴀɢ •\n├───────────────────⦿\n│❍ • ᴛʏᴘᴇ /ʙᴀɴᴀʟʟ ᴛᴏ ꜱᴇᴇ ᴍᴀɢɪᴄ ɪɴ │ • ɢʀᴏᴜᴘ •\n│❍ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➛ [ʙᴧʙʏ-ᴍᴜsɪᴄ™](https://t.me/BABY09_WORLD) • \n╰───────────────────⦿",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴏᴡɴᴇʀ ᴀʟᴘʜ", url=f"https://t.me/{OWNER}")
                ]       
            ]
        )
    )

    # Send a detailed log message to the logger group with user info
    await client.send_message(
        chat_id=LOGGER_GROUP_ID,
        text=f"**{client.me.mention} Logger :**\n\n{user_mention} just started the bot\nuser id: {user_id}\nUsername: {user_username}"
    )


# Send a startup log message to the logger group when the bot starts
async def send_startup_log(client):
    bot_mention = client.me.mention
    bot_id = client.me.id
    bot_username = client.me.username if client.me.username else "No Username"
    current_time = get_indian_time()  # Get the current time in IST

    # Send the startup log message to the logger group
    await client.send_message(
        chat_id=LOGGER_GROUP_ID,
        text=f"**{bot_mention} started**\n"
             f"id: {bot_id}\n"
             f"username: {bot_username}\n"
             f"Time: {current_time}"
    )


# Start the bot
if __name__ == "__main__":
    app.start()  # Start the client
    # Send the startup log message after the bot starts
    app.loop.run_until_complete(send_startup_log(app)) 
    logging.info("Banall-Bot Booted Successfully")
    idle()
