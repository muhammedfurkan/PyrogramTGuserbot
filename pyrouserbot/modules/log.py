from pyrouserbot import app, cmd
import pyrouserbot.herokulog
import os, asyncio, subprocess, sys, time, glob, logging
from datetime import datetime
fileList = glob.glob('pyrouserbot/log/*')
import pyrogram
from pyrogram import *
import tracemalloc
tracemalloc.start()

newest_folder = max(fileList, key=os.path.getmtime)

@Client.on_message(Filters.command("log", cmd) & Filters.me)
async def _logs(client, message: Message):
      try:

        latest_file = max(fileList, key=os.path.getctime)

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
