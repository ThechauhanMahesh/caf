import logging 
import constants
from pyrogram.types import Message
from pyrogram import Client, filters

logging.basicConfig(level=logging.WARN)

app = Client(
    "userbot", 
    api_id=constants.API_ID,
    api_hash=constants.API_HASH,
    session_string=constants.SESSSION_STRING
)

@app.on_message(filters=filters.chat(constants.SOURCE_CHANNEL) & filters.regex(r'🔥'))
# @app.on_message(filters=filters.chat(constants.SOURCE_CHANNEL))
async def forward_message(_, message: Message):

    if not message.reply_to_message_id in constants.SOURCE_TOPIC:
        return 

    # if message.media: return # uncomment to ignore messages with media 

    await message.copy(constants.TARGET_CHANNEL) # to copy message
    # await message.forward(constants.TARGET_CHANNEL) # to forward message

if __name__ == "__main__":
    app.run()
