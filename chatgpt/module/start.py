# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from pyrogram import Client as ren
from pyrogram import *
from pyrogram.types import *
from chatgpt.database import cli

collection = cli["chatgpt"]["users"]

@ren.on_message(filters.command("start") & filters.private)
async def start_bot(c: Client, m: Message):
    user_id = m.from_user.id
    first_name = m.from_user.first_name
    user = {"name": first_name, "_id": user_id}
    
    await collection.update_one({"_id": user_id}, {"$set": user}, upsert=True)
    start_welcome = f"Hey {m.from_user.mention}\n\nWelcome to my bot! Send me a message and I will use the OpenAI API to generate a response.\n\nExample `/ask hello world`"
    start_button = InlineKeyboardMarkup([[InlineKeyboardButton("ADD ME", url=f"https://t.me/{c.me.username}?startgroup=True")]])
    await m.reply_text(start_welcome, reply_markup=start_button)
