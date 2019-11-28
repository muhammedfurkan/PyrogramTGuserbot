import pyrogram
from pyrogram import *
from pyrouserbot import cmd
from time import sleep
import os, sys

@Client.on_message(Filters.command("restart", cmd) & Filters.me)
async def restart(client, message):
    await message.edit("Bot restarted...")
    sleep(2)
    await message.delete()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
