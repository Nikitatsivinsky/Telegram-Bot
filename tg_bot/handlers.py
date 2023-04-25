import json
import os

from tg_bot.models import *
import requests
from .app.novaposhta import NovaPoshta

TG_BASE_URL = 'https://api.telegram.org/bot'


class User:
    user_in_db = None

    def __init__(self, first_name, id, is_bot, language_code, username=None, last_name=None, user_phone_number=None):
        self.first_name = first_name
        self.user_chat_id = id
        self.is_bot = is_bot
        self.language_code = language_code
        self.last_name = last_name
        self.username = username
        self.user_phone_number = user_phone_number
        if self.user_phone_number is None:
            try:
                user_telephone = Profile.query.filter_by(telegram_id=self.user_chat_id).first()
                self.user_phone_number = user_telephone.telephone
            except Exception:
                pass
        self.user_in_db = self.authentification()
        self.register_t_bot_user_id()

    def authentification(self):
        try:
            return Profile.query.filter_by(telephone=self.user_phone_number).first()
        except Exception as ex:
            print("PROBLEMS WITH USER AUTHENTIFICATION")
            print(ex)

    def register_t_bot_user_id(self):
        if self.user_in_db:
            try:
                if self.user_in_db.telegram_id != self.user_chat_id:
                    self.user_in_db.telegram_id = int(self.user_chat_id)
                    db.session.commit()
                else:
                    pass
            except Exception as ex:
                print("PROBLEMS WITH USER register_t_bot_user_id")
                print(ex)


class TelegramHandler:
    user = None

    def __init__(self, bot_token):
        self.bot_token = bot_token

    def send_markup(self, text, markup):
        if self.user.user_chat_id:
            data = {
                'chat_id': self.user.user_chat_id,
                'text': text,
                'reply_markup': markup
            }
            requests.post(f'{TG_BASE_URL}{self.bot_token}/sendMessage', json=data)

    def send_message(self, text, chat_id=None):
        if self.user:
            data = {
                'chat_id': self.user.user_chat_id,
                'text': text
            }
        else:
            data = {
                'chat_id': chat_id,
                'text': text
            }
        requests.post(f'{TG_BASE_URL}{self.bot_token}/sendMessage', json=data)

    def send_contact(self, chat_id=None):
        if self.user:
            if self.user.user_in_db:
                self.send_start_massage()
            data = {
                'chat_id': self.user.user_chat_id,
                'text': 'Для коректної роботи надішліть номер телефону.',
                'reply_markup': {
                    'keyboard': [
                        [{
                            'text': 'Надіслати номер телефону',
                            'request_contact': True
                        }]
                    ],
                    'one_time_keyboard': True,
                    'resize_keyboard': True
                }
            }
        else:
            data = {
                'chat_id': chat_id,
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

        requests.post(f'{TG_BASE_URL}{self.bot_token}/sendMessage', json=data)

    def send_start_massage(self):
        button_my_orders = {
            'text': f'Мої замовлення',
            'callback_data': json.dumps({'route': '/orders'})
        }

        site = {
            'text': f'Перейти на сайт',
            'callback_data': json.dumps({'route': '/site'})
        }
        markup = {
            'inline_keyboard': [[button_my_orders], [site]]
        }
        self.send_markup('Оберіть, що ви хочете зробити?', markup)


class MessageHandler(TelegramHandler):
    def __init__(self, data, bot_token):
        super().__init__(bot_token)
        try:
            if self.user:
                if self.user.user_in_db:
                    self.send_message(f'Вітаю, {self.user.first_name}!')
                    self.send_start_massage()
                else:
                    self.send_message(
                        f'Пробачте {self.user.first_name}, але вас немаэ в нашій Базі Данних Замовників.\n'
                        f'Можливо ви рееструвалися за іншим номером телефону.'
                        f'Реестрація на сайті: https://nikitatsivinsky.github.io/')
            else:
                self.user = User(**data.get('from'), user_phone_number=data.get('contact').get('phone_number'))
                self.send_message(f'Вітаю, {self.user.first_name}!')
                self.send_start_massage()
                self.incoming_message = data.get('text')
        except AttributeError:
            chat_id = data['from'].get('id')
            data = {
                'chat_id': chat_id,
                'text': 'Введіть будь ласка валідні данні.'
            }
            requests.post(f'{TG_BASE_URL}{self.bot_token}/sendMessage', json=data)
            self.send_contact(chat_id)

    def handle(self):
        if self.user:
            if self.user.user_phone_number is None:
                self.send_contact()
            elif self.incoming_message:
                match self.incoming_message.split():
                    case '/start':
                        self.send_start_massage()
                    case ['message']:
                        self.send_message('test message')
                    case _:
                        self.send_start_massage()


class CallbackHandler(TelegramHandler):
    def __init__(self, data, bot_token):
        super().__init__(bot_token)

        if not self.user:
            self.user = User(**data.get('from'))
        self.callback_data = json.loads(data.get('data'))

    def handle(self):
        match self.callback_data:
            case {'route': url}:
                match url:
                    case '/orders':
                        if self.user.user_in_db:
                            orders_list = Order.query.filter(Order.user_id == int(self.user.user_in_db.id)).all()
                            orders_buttoms = []
                            # TODO Pagination ?
                            if orders_list:
                                for order in orders_list:
                                    orders_buttoms.append([{
                                        'text': f'Номер замовлення: {order.id}',
                                        'callback_data': json.dumps({'order_id': str(order.id)})
                                    }])

                                markup = {
                                    'inline_keyboard': orders_buttoms
                                }
                                self.send_markup('Оберіть замовлення', markup)
                            else:
                                self.send_message('Вибачте у Вас немає замовлень.')
                                self.send_start_massage()
                        else:
                            self.send_contact()
                    case '/site':
                        self.send_message('https://nikitatsivinsky.github.io/')
                        self.send_start_massage()

            case {'order_id': order_id}:
                order = Order.query.filter(Order.id == int(order_id)).first()
                button_order_id = {
                    'text': f'Відстежити посилку',
                    'callback_data': json.dumps({'tracking': str(order.ttn)})
                }
                markup = {
                    'inline_keyboard': [[button_order_id]]
                }
                self.send_markup('Оберіть, що ви хочете зробити?', markup)

            case {'tracking': ttn}:
                novaposhta = NovaPoshta(phone=str(self.user.user_phone_number), document_number=ttn,
                                        api_key=os.getenv('NOVA_POSHTA_API_KEY'))
                tracking_status = novaposhta.get_status()
                tracking_str_response = f"\nСтату посылки - {tracking_status['data'][0]['Status']} \n\n " \
                                        f"Посылка № {ttn} от {tracking_status['data'][0]['SenderFullNameEW']}\n" \
                                        f"к {tracking_status['data'][0]['RecipientFullName']},\n" \
                                        f"выехала {tracking_status['data'][0]['DateScan']} \n" \
                                        f"из {tracking_status['data'][0]['WarehouseSenderAddress']}\n" \
                                        f"и едет в {tracking_status['data'][0]['RecipientAddress']}.\n" \
                                        f"Ориентировочная дата доставки {tracking_status['data'][0]['ActualDeliveryDate']},\n" \
                                        f"просим забрать посылку до {tracking_status['data'][0]['DatePayedKeeping']}," \
                                        f" т.к. это дата начала платного сохранения посылки."
                self.send_message(tracking_str_response)
                self.send_start_massage()
