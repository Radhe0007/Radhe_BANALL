import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID", "16457832"))
API_HASH = os.getenv("API_HASH", "3030874d0befdb5d05597deacc3e83ab")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7538146982:AAGeiAfuNVs-gEK1gfOHcPuwbv_5JCv2nvo")
LOGGER_GROUP_ID = int(os.getenv("LOGGER_GROUP_ID", "-1002043570167"))  # लॉगर ग्रुप ID
OWNER = os.getenv("OWNER", "BABY09_WORLD")

# pyrogram client
app = Client(
            "banall",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)

@app.on_message(
filters.command("start")
& filters.private            
)
async def start_command(client, message: Message):
  await message.reply_photo(
                            photo = f"https://telegra.ph/file/62e2e9fc93cd51219264f.jpg",
                            caption=f"╭───────────────────⦿\n│❍ • ʜᴇʏ ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ ʙᴀɴ •\n│❍ • ᴀʟʟ ʙᴏᴛ ᴡʜɪᴄʜ ɪs ʙᴀsᴇᴅ ᴏɴ •\n│• ᴘʏʀᴏɢʀᴀᴍ •\n│❍ • ʟɪʙʀᴀʀʏ ᴛᴏ ʙᴀɴ ᴏʀ ᴅᴇsᴛʀᴏʏ •\n│❍ • ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ᴀ ɢʀᴘ •\n│• ᴡɪᴛʜ ɪɴ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs •\n│❍ • ɴᴏ sᴛᴏᴘ + ɴᴏ ʟᴀɢ •\n├───────────────────⦿\n│❍ • ᴛʏᴘᴇ /ʙᴀɴᴀʟʟ ᴛᴏ ꜱᴇᴇ ᴍᴀɢɪᴄ ɪɴ │ • ɢʀᴏᴜᴘ •\n│❍ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➛ [ʙᴧʙʏ-ᴍᴜsɪᴄ™](https://t.me/BABY09_WORLD) • \n╰───────────────────⦿",
  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ ᴀʟᴘʜ", url=f"https://t.me/{OWNER}")
                ]       
           ]
      )
)
await client.send_message(
            chat_id=LOGGER_GROUP_ID,
            text=f"{user_mention} just started the bot!"
)

@app.on_message(
filters.command("banall") 
& filters.group
)
async def banall_command(client, message: Message):
    print("getting memebers from {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id = message.chat.id, user_id = i.user.id)
            print("kicked {} from {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("failed to kicked {} from {}".format(i.user.id, e))           
    print("process completed")
    

# start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()
