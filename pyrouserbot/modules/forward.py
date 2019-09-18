import pyrogram, os, time
from pyrogram import Filters, Client
from pyrouserbot import app, cmd

@Client.on_message(Filters.command(["fwd"], cmd) & Filters.me)
async def for_ward(client, message):
      FORWARD_TARGET=os.environ.get("FORWARD_ID")
      if not FORWARD_TARGET:
         await message.edit("You have to add Forward Target id")
         time.sleep(5)
         await message.delete()
      if message.reply_to_message:
         await message.reply_to_message.forward(chat_id=FORWARD_TARGET)
         time.sleep(5)
         await message.delete()
      else:
         await message.edit("You have to reply to a document for Forward")
         time.sleep(5)
         await message.delete()
         
