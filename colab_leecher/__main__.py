import logging, os
from pyrogram import filters
from datetime import datetime
from pyrogram.errors import BadRequest
from asyncio import sleep, get_event_loop
from colab_leecher import colab_bot, OWNER
from .utility.task_manager import taskScheduler
from colab_leecher.utility.handler import cancelTask
from .utility.variables import BOT, MSG, BotTimes, Paths
from .utility.helper import isLink, setThumbnail, message_deleter
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

src_request_msg = None


@colab_bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.delete()
    text = "**Hey There, 👋🏼 It's Colab Leecher**\n\n◲ I am a Powerful File Transloading Bot 🚀\n◲ I can Transfer Files To Telegram or Your Google Drive From Various Sources 🦐"
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Repository 🦄", url="https://github.com/Xrontrix10/Telegram-Leecher"
                ),
                InlineKeyboardButton("Support 💝", url="https://t.me/Colab_Leecher"),
            ],
        ]
    )
    await message.reply_text(text, reply_markup=keyboard)


@colab_bot.on_message(filters.command("colabxr") & filters.private)
async def colabxr(client, message):
    global BOT, src_request_msg
    text = "<b>◲ Send Me DOWNLOAD LINK(s) 🔗»\n◲</b> <i>You can enter multiple links in new lines and I will download each of them 😉 </i>"
    await message.delete()
    BOT.State.started = True
    src_request_msg = await message.reply_text(text)


async def send_settings(client, message, msg_id, command: bool):
    # Function code remains the same


@colab_bot.on_message(filters.command("settings") & filters.private)
async def settings(client, message):
    if message.chat.id == OWNER:
        await message.delete()
        await send_settings(client, message, message.id, True)


@colab_bot.on_message(filters.create(isLink) & ~filters.photo)
async def handle_url(client, message):
    global BOT

    # Reset
    BOT.Options.custom_name = ""
    BOT.Options.zip_pswd = ""
    BOT.Options.unzip_pswd = ""

    temp_source = message.text.splitlines()

    # Check for arguments in message
    for _ in range(3):
        if temp_source[-1][0] == "[":
            BOT.Options.custom_name = temp_source[-1][1:-1]
            temp_source.pop()
        elif temp_source[-1][0] == "{":
            BOT.Options.zip_pswd = temp_source[-1][1:-1]
            temp_source.pop()
        elif temp_source[-1][0] == "(":
            BOT.Options.unzip_pswd = temp_source[-1][1:-1]
            temp_source.pop()
        else:
            break

    if BOT.State.started:
        BOT.SOURCE.extend(temp_source)
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Leech", callback_data="leech"),
                    InlineKeyboardButton("Mirror", callback_data="mirror"),
                ],
                [InlineKeyboardButton("Dir-Leech", callback_data="dir-leech")],
            ]
        )
        await message.reply_text(
            text="<b>◲ Choose COLAB LEECHER Operation MODE For This Current Task 🍳 »</b>",
            reply_markup=keyboard,
            quote=True,
        )
    else:
        await message.reply_text(
            "<i>Send /colabxr to start a new task first!</i>",
            quote=True
        )


@colab_bot.on_callback_query()
async def handle_options(client, callback_query):
    # Function code remains the same


@colab_bot.on_message(filters.photo & filters.private)
async def handle_image(client, message):
    # Function code remains the same


@colab_bot.on_message(filters.command("setname") & filters.private)
async def custom_name(client, message):
    # Function code remains the same


@colab_bot.on_message(filters.command("zipaswd") & filters.private)
async def zip_pswd(client, message):
    # Function code remains the same


@colab_bot.on_message(filters.command("unzipaswd") & filters.private)
async def unzip_pswd(client, message):
    # Function code remains the same


@colab_bot.on_message(filters.command("help") & filters.private)
async def help_command(client, message):
    # Function code remains the same


logging.info("Colab Leecher Started !")
colab_bot.run()
