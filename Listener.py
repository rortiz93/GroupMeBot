import os
import json

import sys

import GroupMeBot
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request
full_text = ''
app = Flask(__name__)

app.route('https://salty-dawn-83243.herokuapp.com/', methods=['POST'])
def webhook():
  data = request.get_json()

  # We don't want to reply to ourselves!
  if data['name'] != 'bitch nutz':
    msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    send_message(msg)

  return "ok", 200


def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': os.getenv('botId'),
        'text': msg,
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


def log(msg):
    print(str(msg))
    sys.stdout.flush()