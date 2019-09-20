import pyrogram
from pyrogram import *
from pyrouserbot import app, cmd


@Client.on_message(Filters.command(["load"],cmd) & Filters.me)
async def lo_ad(client, message):
      pname = message.text[6:]
      fpname = "pyrouserbot.modules."+pname
      try:
          client.add_handler(*fpname)
      except Exception as e:
          message.reply(str(e))
      
      
