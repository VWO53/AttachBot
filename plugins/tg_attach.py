#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala


#configs for the bot
from config import Config

from telegram import ParseMode

def attach(update, context):
  if update.message.reply_to_message == None:
    update.message.reply_text("""**Hei Follow These Steps..**

1. Send any File/media

2. Reply Then Add text which you want to generate the attached post.

**Available Commands..**

/start - ```Check The Bot Is Online Or Offline```
/help - `How To Use Me`""")
  else:
    m = context.bot.forward_message("@" + Config.CHANNEL_USERNAME, update.effective_chat.id, update.message.reply_to_message.message_id)
    m_id = m.message_id
    link = "https://t.me/{}/{}".format(Config.CHANNEL_USERNAME, m_id)
    print(link)
    context.bot.send_message(update.effective_chat.id, update.message.text + "[{}]({})".format("\u2063", link), parse_mode=ParseMode.MARKDOWN)
