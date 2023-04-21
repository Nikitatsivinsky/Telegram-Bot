from tg_bot import app,db
from flask import request, redirect, jsonify
from .handlers import MessageHandler, CallbackHandler
from tg_bot.models import *



@app.route('/', methods=['POST'])
def main_route():
    request_json = request.json
    print(request_json)
    if message := request_json.get('message'):
        handler = MessageHandler(message)
    elif callback := request_json.get('callback_query'):
        handler = CallbackHandler(callback)
    else:
        return jsonify({'message': 'Invalid request'}), 400
    handler.handle()
    return 'Ok'


# @app.route('/', methods=['GET'])
# def main_route():
#     test = Test(
#         id=1,
#         username='nikitatsiv',
#         email='nikitatsiv@gmail',
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

