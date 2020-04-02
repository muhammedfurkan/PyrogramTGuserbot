from datetime import datetime
from pyrogram import Client, Filters

from pyrouserbot import cmd


@Client.on_message(Filters.command(["ping"],cmd) & Filters.me)
async def pi_ng(client, message):
      start = datetime.now()
      await message.edit("Pong!")
      end = datetime.now()
      ms = (end - start).microseconds / 1000
      await message.edit("Pong!\n{} ms".format(ms))
