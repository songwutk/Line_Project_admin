from __future__ import unicode_literals
import json
import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FileMessage , ImageMessage , FollowEvent ,sources,FollowEvent
)


from Project import app

from Project import line_bot_api,parser

from Project.RichMenu import menuList,postmenu



@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        events = parser.parse(body, signature)

    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)


################### cannot read event ################

    for event in events:
        user_id= event.source.sender_id
        line_bot_api.link_rich_menu_to_user(user_id,'richmenu-7c7946aded99dab8c2ab94986b6a0c1d')
        if isinstance(event, MessageEvent):
            menuname = event.message.text
            postmenu(menuname,user_id)

        if isinstance(event, FollowEvent):
            line_bot_api.link_rich_menu_to_user(user_id,'richmenu-7c7946aded99dab8c2ab94986b6a0c1d')

    

    return 'OK'


