import os
import logging
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# लॉगिंग सेटअप
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Config vars
API_ID = int(os.getenv("API_ID", "16457832"))
API_HASH = os.getenv("API_HASH", "3030874d0befdb5d05597deacc3e83ab")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7538146982:AAGeiAfuNVs-gEK1gfOHcPuwbv_5JCv2nvo")
OWNER = os.getenv("OWNER", "BABY09_WORLD")

# Pyrogram client
app_pyrogram = Client(
    "banall",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# /start कमांड का हैंडलर
@app_pyrogram.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    user_mention = message.from_user.mention  # यूजर का मेंशन नाम प्राप्त करें
    try:
        logging.info("Received /start command")
        
        # बॉट का संदेश उपयोगकर्ता को भेजें
        await message.reply_photo(
            photo="https://telegra.ph/file/62e2e9fc93cd51219264f.jpg",
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
        logging.info(f"Start command logged for {message.from_user.id}")
    except Exception as e:
        logging.error(f"Failed to handle start command: {e}")

# Pyrogram बॉट को चालू करने के लिए
async def run_pyrogram():
    await app_pyrogram.start()
    print("Bot Started Successfully")
    await app_pyrogram.idle()  # Pyrogram idle method, जो बॉट को चालू रखेगा

# मुख्य एंट्री पॉइंट
if __name__ == "__main__":
    import asyncio
    asyncio.run(run_pyrogram())
