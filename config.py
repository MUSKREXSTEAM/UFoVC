import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ᴜғᴏ ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/b1fe76175bcf213770ca6.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/b1fe76175bcf213770ca6.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/b1fe76175bcf213770ca6.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b1fe76175bcf213770ca6.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "MEUZKBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "KKKKGU")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "GVVVV6")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "QQOQQD")
OWNER_NAME = getenv("OWNER_NAME", "KKKKGU") 
DEV_NAME = getenv("DEV_NAME", "KKKKGU")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
