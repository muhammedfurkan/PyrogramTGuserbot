import pyrogram
from pyrogram import *
from pyrouserbot import app, cmd
import pyrouserbot

@Client.on_message(Filters.command(["load"],cmd) & Filters.me)
async def lo_ad(client, message):
      pname = message.text[6:]
      fpname = "pyrouserbot.modules."+pname
      path = "/app/pyrouserbot/modules/"+pname+".py"
      if not os.path.isfile(path):
            await message.reply(f"There is no module named {pname}")
            return
         
      try:
          client.add_handler(fpname)
          await message.reply(f"Successfully loaded {pname}")
      except Exception as e:
          await message.reply(str(e))
      
      
