# encoding: utf-8
import json
import requests

from .resource import AbstractResource
from .settings import BASE_URL


class Recipient(AbstractResource):
    BASE_URL = BASE_URL + 'recipients'

    def __init__(
            self,
            api_key=None,
            id=None,
            count=None,
            page=None,
            transfer_interval=None,
            transfer_day=None,
            transfer_enabled=None,
            bank_account_id=None,
            bank_account=None):

        if bank_account_id:
            self.data = {
                'transfer_interval': transfer_interval,
                'transfer_day': transfer_day,
                'transfer_enabled': transfer_enabled,
                'bank_account_id': bank_account_id,
                'bank_account': bank_account                              
            }
        else:
            self.data = {}
            if id:
                self.data['id'] = id
            else:
                if count:
                    self.data['count'] = count
                if page:
                    self.data['page'] = page
        self.data['api_key'] = api_key


    def handle_response(self, data):
        self.id = data['id']
        self.transfer_interval = data['transfer_interval']
        self.transfer_day = data['transfer_day']
        self.transfer_enabled = data['transfer_enabled']
        self.bank_account = data['bank_account']

    def get_data(self):
        return self.data

    def find_by_id(self):
        bank_id = self.data['id']    
        url = self.BASE_URL + '/' + str(bank_id)   
        pagarme_response = requests.get(url, params={'api_key': self.data['api_key']})
        if pagarme_response.status_code == 200:
            self.handle_response(json.loads(pagarme_response.content.decode(encoding='UTF-8')))
        else:
            self.error(json.loads(pagarme_response.content.decode(encoding='UTF-8')))
            
    def find_all(self):
        url = self.BASE_URL + '/'      
        pagarme_response = requests.get(url, params={'api_key': self.data['api_key']})
            
        if pagarme_response.status_code == 200:
            list_banks = json.loads(pagarme_response.content.decode(encoding='UTF-8'))
            return list_banks
        else:
            self.error(json.loads(pagarme_response.content.decode(encoding='UTF-8')))       
                