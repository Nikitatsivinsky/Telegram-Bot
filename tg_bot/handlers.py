import json

import requests

BOT_TOKEN = '6087432712:AAGTC7aT4dtYcqXMt--m1pV3ZGjcEUjGIo8'  # TODO move to env
TG_BASE_URL = 'https://api.telegram.org/bot'

user_phone_number = None

class User:
    def __init__(self, first_name, id, is_bot, language_code, last_name, username):
        self.first_name = first_name
        self.id = id
        self.is_bot = is_bot
        self.language_code = language_code
        self.last_name = last_name
        self.username = username



class TelegramHandler:
    user = None

    def send_markup(self, text, markup):
        data = {
            'chat_id': self.user.id,
            'text': text,
            'reply_markup': markup
        }
        requests.post(f'{TG_BASE_URL}{BOT_TOKEN}/sendMessage', json=data)

    def send_message(self, text):
        data = {
            'chat_id': self.user.id,
            'text': text
        }
        requests.post(f'{TG_BASE_URL}{BOT_TOKEN}/sendMessage', json=data)


    def send_contact(self):
        data = {
            'chat_id': self.user.id,
            'text': 'Для корректной работы, отправте номер телефона.',
            'reply_markup': {
                'keyboard': [
                    [{
                        'text': 'Отправить номер телефона',
                        'request_contact': True
                    }]
                ],
                'one_time_keyboard': True,
                'resize_keyboard': True
            }
        }

        requests.post(f'{TG_BASE_URL}{BOT_TOKEN}/sendMessage', json=data)

    def send_start_massage(self):
        button_tracking = {
            'text': f'Выбрать товар для отслеживания',
            'callback_data': json.dumps({'route': '/items'})
        }
        markup = {
            'inline_keyboard': [[button_tracking]]
        }
        self.send_markup('Выберите что вы хотите сделать?', markup)


class MessageHandler(TelegramHandler):
    def __init__(self, data):
        self.user = User(**data.get('from'))
        self.incoming_message = data.get('text')

        if contact := data.get('contact'):
            global user_phone_number
            user_phone_number = contact.get('phone_number')
            self.send_message(f'Привет {self.user.first_name}!')
            self.send_start_massage()


    def handle(self):
        if user_phone_number is None:
            self.send_contact()
        elif self.incoming_message:
            match self.incoming_message.split():
                case 'test', value:
                    test_button = {
                        'text': f'value {value}',
                        'callback_data': json.dumps({'test': 'data'})
                    }
                    markup = {
                        'inline_keyboard': [[test_button], [test_button], [test_button]]
                    }
                    self.send_markup('test markup', markup)

                case ['message']:
                    self.send_message('test message')

                case _:
                    self.send_start_massage()




class CallbackHandler(TelegramHandler):
    def __init__(self, data):
        self.user = User(**data.get('from'))
        self.callback_data = json.loads(data.get('data'))

    def handle(self):
        match self.callback_data['route']:
            case '/items':
                print('ENTER items')
