import os

import requests
from flask import json


class NovaPoshta:

    def __init__(self, api_key: str, phone: str, document_number: str):
        self.api_key = api_key
        self.document_number = document_number
        self.phone = phone

    def get_status(self):
        url = 'https://api.novaposhta.ua/v2.0/json/getStatusDocuments'
        data_dict = {
            "apiKey": f"{self.api_key}",
            "modelName": "TrackingDocument",
            "calledMethod": "getStatusDocuments",
            "methodProperties": {
                "Documents": [
                    {
                        "DocumentNumber": f"{self.document_number}",
                        "Phone": f"{self.phone}"
                    }
                ]
            }
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(url, data=json.dumps(data_dict), headers=headers)
        json_str = response.content.decode('utf-8')
        return json.loads(str(json_str))