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


if __name__ == '__main__':
    document_number = '20400322842042'
    novaposhta = NovaPoshta(phone='380669184215', document_number=document_number,
                            api_key='d274212c55ef2a0178786d3e14547337')
    tracking_status = novaposhta.get_status()
    if tracking_status['success']:
        print(f"\nСтату посылки - {tracking_status['data'][0]['Status']} \n\n"
              f"Посылка № {document_number} от {tracking_status['data'][0]['SenderFullNameEW']}\n"
              f"к {tracking_status['data'][0]['RecipientFullName']},\n"
              f"выехала {tracking_status['data'][0]['DateScan']} \n"
              f"из {tracking_status['data'][0]['WarehouseSenderAddress']}\n"
              f"и едет в {tracking_status['data'][0]['RecipientAddress']}.\n"
              f"Ориентировочная дата доставки {tracking_status['data'][0]['ActualDeliveryDate']},\n"
              f"просим забрать посылку до {tracking_status['data'][0]['DatePayedKeeping']},"
              f" т.к. это дата начала платного сохранения посылки.")
    else:
        print(f"Error request in NovaPoshta: {tracking_status['errors']}")
