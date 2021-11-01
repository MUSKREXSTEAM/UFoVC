from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

from callsmusic import callsmusic, queues

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT, UPDATES_CHANNEL, AUD_IMG, QUE_IMG, OWNER_NAME
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(command("play") & other_filters)
@errors
async def stream(_, message: Message):

    lel = await message.reply("جاري التشغيل انتظر 🤝..")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="قناة السورس",
                        url=f"https://t.me/{UPDATES_CHANNEL}"),
                    InlineKeyboardButton(
                        text="الحساب المساعد",
                        url=f"https://t.me/{OWNER_NAME}")
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"✘ ᴠɪᴅᴇᴏs ʟᴏɴɢᴇʀ ᴛʜᴀɴ {DURATION_LIMIT} ᴍɪɴᴜᴛᴇ(s) ᴀʀᴇɴ'ᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴘʟᴀʏ!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("قم بالرد على رابط او ملف التشغيل ")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo=f"{QUE_IMG}",
        reply_markup=keyboard,
        caption=f"#⌛ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴡᴀs ᴀᴅᴅᴇᴅ ᴛᴏ **ǫᴜᴇᴜᴇ** ᴀᴛ ᴘᴏsɪᴛɪᴏɴ {position}!\n\n✈ ᴘᴏᴡᴇʀᴇᴅ ʙʏ {bn}")
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        costumer = message.from_user.mention
        await message.reply_photo(
        photo=f"{AUD_IMG}",
        reply_markup=keyboard,
        caption=f"🎧 **تم الطلب** بواسطت {costumer} !\n\n سورس ميلانو  {bn}"
        )   
        return await lel.delete()
