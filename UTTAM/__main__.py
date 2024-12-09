import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

# Logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Config vars (Use environment variables if running on server)
API_ID = int(os.getenv("API_ID", "16457832"))
API_HASH = os.getenv("API_HASH", "3030874d0befdb5d05597deacc3e83ab")
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

@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    user_mention = message.from_user.mention  # Get user's mention
    
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

    # Log the start command usage
    await client.send_message(
        chat_id=LOGGER_GROUP_ID,
        text=f"{user_mention} just started the bot!"
    )


@app.on_message(filters.command("banall") & filters.group)
async def banall_command(client, message: Message):
    # Log the group ID where the banall command was used
    logging.info(f"Getting members from {message.chat.id}")
    
    try:
        async for member in app.get_chat_members(message.chat.id):
            try:
                # Attempt to ban each member
                await app.ban_chat_member(chat_id=message.chat.id, user_id=member.user.id)
                logging.info(f"Banned {member.user.id} from {message.chat.id}")
            except ChatAdminRequired:
                logging.warning(f"Bot is not an admin in {message.chat.id}, cannot ban members.")
            except Exception as e:
                logging.error(f"Failed to ban {member.user.id} from {message.chat.id}: {e}")
        logging.info("Ban all process completed.")
    except Exception as e:
        logging.error(f"Error during banning members in {message.chat.id}: {e}")


# Start the bot
if __name__ == "__main__":
    app.start()
    logging.info("Banall-Bot Booted Successfully")
    idle()
