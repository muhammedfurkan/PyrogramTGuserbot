from datetime import datetime
import requests
from pyrogram import Client, Filters
from pyrouserbot import cmd


@Client.on_message(Filters.command(["xtools"], cmd) & Filters.me)
async def xtools(client, message):
    message_text = message.text[8:]
    start = datetime.now()
    sub_domain, username = message_text.split("|")
    url = "https://xtools.wmflabs.org/api/user/simple_editcount/{}.wikipedia.org/{}".format(sub_domain, username)
    json_string = requests.get(url).json()
    result_text = json_string["liveEditCount"]
    end = datetime.now()
    ms = (end - start).seconds
    text_message = "edit count of {} ({}) in {} seconds. \n {}".format(
        username, sub_domain, str(ms), result_text)
    await message.edit(text_message)
