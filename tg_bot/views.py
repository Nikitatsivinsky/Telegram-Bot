from tg_bot import app,db
from flask import request, redirect, jsonify
from .handlers import MessageHandler, CallbackHandler
from tg_bot.models import *
import os



@app.route('/', methods=['POST'])
def main_route():
    request_json = request.json
    print(request_json)
    if message := request_json.get('message'):
        handler = MessageHandler(data=message, bot_token=os.getenv('TG_TOKEN'))
    elif callback := request_json.get('callback_query'):
        handler = CallbackHandler(data=callback, bot_token=os.getenv('TG_TOKEN'))
    else:
        return jsonify({'message': 'Invalid request'}), 400
    handler.handle()
    return 'Ok'


