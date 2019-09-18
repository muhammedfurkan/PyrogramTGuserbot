import pyrogram
from pyrogram import Client, Filters
from pyrouserbot import app, cmd

@Client.on_message(Filters.command("restart", cmd) & Filters.me)
async def _restart(bot, message, app):
      await app.stop()
      await app.restart()
      await message.edit('Restart complete.')
