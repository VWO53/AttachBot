#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala


#Secret configs
from config import Config


def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello [{update.message.from_user.first_name}](tg://user?id={update.message.from_user.id}) This is Telegram Attach Bot!\n\n```You Can Attach Any Telegram Media With Your Long text```\n\nDo One By One Other Wise You Will Get Permanent Ban\n\nchannel:- © @TG_BotZ\n\n/help For More Details", parse_mode="Markdown")
