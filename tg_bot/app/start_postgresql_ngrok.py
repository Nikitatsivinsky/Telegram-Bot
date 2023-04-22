import subprocess
from pyngrok import ngrok
import requests
import json


class StartProcess:
    cmd = None
    name = None
    def startprocess(self):
        try:
            subprocess.call(self.cmd, shell=True)
        except Exception as ex:
            print(f'Something went wrong when start {self.name} {ex}' )


class StartPostgresqlServer(StartProcess):
    """ Class Starting PostgreSQL server, if you see massage: '[sudo] password for username:'
     on Ubuntu you can edit sudoers file (sudo visudo) by 'username ALL=NOPASSWD:/usr/sbin/service postgresql start'
     to delete this massage.
    """
    def __init__(self, password):
        self.cmd = f'echo {password} | sudo -S service postgresql start'
        self.name = 'PostgreSQL Server'
        self.startprocess()


class StartNGROK:
    def __init__(self, port, tg_token):
        self.port = port
        self.tg_token = tg_token
        self.ngrok_url = None

        self.start()
        self.register_webhook()

    def start(self):
        # запуск ngrok
        http_tunnel = ngrok.connect(self.port)
        # получение URL, по которому можно получить доступ к туннелю
        self.ngrok_url = http_tunnel

    def register_webhook(self):
        tg_url = f'https://api.telegram.org/bot{self.tg_token}/setWebhook'
        data_dict = {
            "url": str(self.ngrok_url.public_url)
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(tg_url, data=json.dumps(data_dict), headers=headers)
        print(f'Status register NGROK: {response} on URL: {self.ngrok_url.public_url}')

