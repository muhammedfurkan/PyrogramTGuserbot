import pyrogram
from pyrogram import *
from pyrouserbot import cmd
from time import sleep
import os, sys

@Client.on_message(Filters.command("restart", cmd) & Filters.me)
def restart(client, message):
    os.execl(sys.executable, sys.executable, *sys.argv)
    message.edit("Bot restarted...")
    sleep(2)
    message.delete()
    quit()
