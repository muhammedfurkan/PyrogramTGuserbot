import glob
import logging
import os
import tracemalloc
from pyrogram import *

import pyrouserbot.herokulog
from pyrouserbot import cmd

fileList = glob.glob('pyrouserbot/log/*')
tracemalloc.start()

newest_folder = max(fileList, key=os.path.getmtime)

@Client.on_message(Filters.command("log", cmd) & Filters.me)
async def _logs(client, message: Message):
      try:

        #latest_file = max(fileList, key=os.path.getctime)

        for fname in fileList:
          if fname != newest_folder:
            print('removing -> %s', fname)
            os.remove(fname)
          else:
            logging.warning("New logged File: "+newest_folder)
            await message.reply_document(newest_folder)
      except FileNotFoundError as e: 
        logging.debug(e)
        pass
