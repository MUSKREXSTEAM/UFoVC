#سالِم
from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ **ᴡᴇʟᴄᴏᴍᴇ {message.from_user.first_name}** \n
⌁ ⁞ ** في بوت تشغيل الاغاني  في المكالمه ' الجماعيه**
⌁ ⁞ **قم برفع البوت مشرف وارسل'الاوامر واختر ماتريد تشغيله**
⌁ ⁞ **العرظ اوامر البوت اظغط في خاص البوت**
⌁ ⁞ **على زر الاوامر او كلمه**, /help**
⌁ ⁞ ** البوت مقدم من سورس ميلانو **
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                         "⌯االاوامر", url="https://t.me/{OWNER_NAME}"
                    ),
                    InlineKeyboardButton(
                        "⌯الحساب المساعد", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "⌯قناة البوت", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "⌯سورس البوت", url=f"https://t.me/QQOQQD")               
                 ],[
                    InlineKeyboardButton(
                        "", url="https://t.me/"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✔ **ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ**\n<b>☣ **ᴜᴘᴛɪᴍᴇ:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⌯ قناة البوت", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>☢ ʜᴇʟʟᴏ {message.from_user.mention()}, ᴘʟᴇᴀsᴇ ᴛᴀᴘ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ sᴇᴇ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇssᴀɢᴇ ʏᴏᴜ ᴄᴀɴ ʀᴇᴀᴅ ғᴏʀ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✔ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?start=help"
                    )
                ]
            ]
        )
    )



@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "✈ `ᴘᴏɴɢ!!`\n"
        f"☣ `{delta_ping * 1000:.3f} ᴍs`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 ʙᴏᴛ sᴛᴀᴛᴜs:\n"
        f"➤ **ᴜᴘᴛɪᴍᴇ:** `{uptime}`\n"
        f"➤ **sᴛᴀʀᴛ ᴛɪᴍᴇ:** `{START_TIME_ISO}`"
    )
