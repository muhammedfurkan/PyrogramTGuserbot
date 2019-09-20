import pyrogram
from pyrogram import *
from pyrouserbot import app, cmd
import plugins

@Client.on_message(Filters.command(["load"],cmd) & Filters.me)
async def lo_ad(client, message):
      pname = message.command[1:]
      fpname = plugins+"."+pname
      try:
          client.add_handler(*fpname)
      except Exception as e:
          message.reply(str(e))
      
      
