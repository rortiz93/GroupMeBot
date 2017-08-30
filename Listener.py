import os
import json
import GroupMeBot
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request
full_text = ''
app = Flask(__name__)

app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  # We don't want to reply to ourselves!
  if data['name'] != 'bitch nutz':
    msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    GroupMeBot.send_message(full_text)

  return "ok", 200