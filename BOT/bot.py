from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import random
import os
from telegraph import upload_file
import pyrogram
from sample_config import Config
import logging


App=Client(
    "Pyrogram bot",
    bot_token="bot token",
    api_id="api id",
    api_hash="api hash"
)




ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg"
]



@app.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('🤔Help', callback_data='help'),
        InlineKeyboardButton('Close🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('support group', url='http://telegram.me/septemberfilms'),
        InlineKeyboardButton('dev', url='t.me/devourdevils')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await devourdevils.send_photo(
        photo=random.choice(ALL_PIC),
        chat_id=message.chat.id,
        caption=f"""hello {message.from_user.mention} iam a bot used for get basic information of your bot""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )

    
    
ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg"
]




@app.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('🏡Home', callback_data='home'),
        InlineKeyboardButton('Close🔐', callback_data='close'),
        InlineKeyboardButton('about', callback_data='about')
    ],
    [
        InlineKeyboardButton('source code', url='https://github.com/kamarjahan/DD-INFORMATIONBOT'),
        
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await devourdevils.send_photo(
        photo=random.choice(ALL_PIC),
        chat_id=message.chat.id,
        caption=f"""hello  {message.from_user.mention},
this is id finding bot made by @devourdevils""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )


@devourdevils.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('🏡Home', callback_data='home'),
        InlineKeyboardButton('Close🔐', callback_data='close') 
    
    
    
    
    await message.reply_text(text=text)
    
    
    
    
    
    

    
    
    
    
    
