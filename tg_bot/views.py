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
        handler = MessageHandler(data=message,bot_token=os.getenv('TG_TOKEN'))
    elif callback := request_json.get('callback_query'):
        handler = CallbackHandler(data=callback,bot_token=os.getenv('TG_TOKEN'))
    else:
        return jsonify({'message': 'Invalid request'}), 400
    handler.handle()
    return 'Ok'
#


# TEST BD
# @app.route('/', methods=['GET'])
# def main_route():
#     test = TestOne(
#         id=1,
#         name='nikitatsiv',
#         test=2,
#     )
#     db.session.add(test)
#     db.session.commit()
#     return 'test doned', 201





# @app.route('/start', methods=['POST'])
# def start():
#
#     update = request.get_json()
#
#     if 'contact' in request.json.get('message'):
#         phone_number = update['message']['contact']['phone_number']
#         print('Номер телефона получен: {}'.format(phone_number))
#     else:
#         handler = MessageHandler(request.json.get('message'))
#         handler.handle()

