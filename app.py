import os
import json

import sys

import GroupMeBot
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request, render_template
full_text = ''
app = Flask(__name__)

app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  print("x")
  GroupMeBot.send_message(full_text)
  # We don't want to reply to ourselves!
  if data['name'] != 'bitch nutz':
    msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    GroupMeBot.send_message(full_text)

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

if __name__ == '__main__':
    app.run()