import pyrogram
from pyrogram import *
from pyrouserbot import app, cmd
import os, pyrouserbot

@Client.on_message(Filters.command(["unload"],cmd) & Filters.me)
async def unl_oad(client, message):
      pname = message.text[8:]
      fpname = "pyrouserbot.modules."+pname
      path = "/app/pyrouserbot/modules/"+pname+".py"
      if not os.path.isfile(path):
            await message.reply(f"There is no module named {pname}")
            return
         
      try:
          client.add_handler(fpname)
          await message.reply(f"Successfully unloaded {pname}")
      except Exception as e:
          await message.reply(str(e))
      
