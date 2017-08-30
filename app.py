import os
import json

import sys

import GroupMeBot
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request, render_template
full_text = ''
app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()


  # We don't want to reply to ourselves!
  if data['name'] != 'bitch nutz':
      if data['text'] == '/score':
          GroupMeBot.send_message(full_text)



  return "ok", 200




def log(msg):
    print(str(msg))
    sys.stdout.flush()

if __name__ == '__main__':
    app.run()