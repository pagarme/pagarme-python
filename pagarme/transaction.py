# encoding: utf-8

import json
import requests

from .exceptions import PagarmeApiError, NotPaidException, NotBoundException
from .resource import AbstractResource


class Transaction(AbstractResource):
    BASE_URL = 'https://api.pagar.me/1/transactions'

    def __init__(
            self,
            api_key=None,
            amount=None,
            card_hash=None,
            card_id=None,
            payment_method='credit_card',
            installments=1,
            postback_url=None,
            metadata={},
            soft_descriptor='',
            customer=None,
            split_rules=None,
            **kwargs):

        self.amount = amount
        self.api_key = api_key
        self.card_hash = card_hash
        self.card_id = card_id
        self.payment_method = payment_method
        self.installments = installments
        self.postback_url = postback_url
        self.metadata = metadata
        self.soft_descriptor = soft_descriptor[:13]
        self.id = None
        self.data = {}
        self.customer = customer
        self.split_rules = split_rules

        for key, value in kwargs.items():
            self.data[key] = value

    def error(self, response):
        try:
            data = json.loads(response)
            e = data['errors'][0]
            error_string = e['type'] + ' - ' + e['message']
            raise PagarmeApiError(error_string)
        except:
            e = response['errors'][0]
            self.error = e['type'] + ' - ' + e['message']

    def charge(self):
        post_data = self.get_data()        
        url = self.BASE_URL
        pagarme_response = requests.post(url, data=post_data)
        if pagarme_response.status_code == 200:
            try:
                self.handle_response(json.loads(pagarme_response.content))
            except:
                self.handle_response(json.loads(pagarme_response.content.decode(encoding='UTF-8')))
        else:
            try:
                self.error(pagarme_response.content)
            except:
                self.error(json.loads(pagarme_response.content.decode(encoding='UTF-8')))

    def handle_response(self, data):
        self.id = data['id']
        self.status = data['status']
        self.card = data['card']
        self.postback_url = data['postback_url']
        self.metadata = data['metadata']
        self.data = data

    def capture(self, _id=None, _amount=None):
        if _id is None:
            if self.id is None:
                raise NotBoundException('First try search your transaction')
        else:
            self.id = _id
            self.amount = _amount
            
        url = self.BASE_URL + '/' + str(self.id) + '/capture'
        print(url)
        if _amount:
            data = {'api_key': self.api_key, 'amount': self.amount}
        else:
            data = {'api_key': self.api_key}
        pagarme_response = requests.post(url, data=data)
        if pagarme_response.status_code == 200:
            try:
                self.handle_response(json.loads(pagarme_response.content))
            except:
                self.handle_response(json.loads(pagarme_response.content.decode(encoding='UTF-8')))
        else:
            try:
                self.error(pagarme_response.content)
            except:
                self.error(json.loads(pagarme_response.content.decode(encoding='UTF-8')))

    def get_data(self):
        return self.__dict__()

    def __dict__(self):
        d = self.data
        d['api_key'] = self.api_key
        if self.amount:
            d['amount'] = self.amount
            d['card_hash'] = self.card_hash
            d['card_id'] = self.card_id
            d['installments'] = self.installments
            d['payment_method'] = self.payment_method
            d['soft_descriptor'] = self.soft_descriptor[:13]
        
        if self.metadata:
            for key, value in self.metadata.items():
                new_key = 'metadata[{key}]'.format(key=key)
                d[new_key] = value

        if self.postback_url:
            d['postback_url'] = self.postback_url

        if self.customer:
            d.update(self.customer.get_anti_fraud_data())
            
        if self.split_rules:
            cont = 0
            for s in self.split_rules: 
                d.update(s.get_split_data(cont))
                cont=cont+1
        return d

    def find_by_id(self, _id=None):
        url = self.BASE_URL + '/' + str(_id)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            try:
                self.handle_response(json.loads(pagarme_response.content))
            except:
                self.handle_response(json.loads(pagarme_response.content.decode(encoding='UTF-8')))
        else:
            try:
                self.error(pagarme_response.content)
            except:
                self.error(json.loads(pagarme_response.content.decode(encoding='UTF-8')))

    def refund(self):
        if self.id is None:
            raise NotPaidException('Id not suplied')

        url = self.BASE_URL + '/' + str(self.id) + '/refund'
        pagarme_response = requests.post(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            try:
                self.handle_response(json.loads(pagarme_response.content))
            except:
                self.handle_response(json.loads(pagarme_response.content.decode(encoding='UTF-8')))
        else:
            try:
                self.error(pagarme_response.content)
            except:
                self.error(json.loads(pagarme_response.content.decode(encoding='UTF-8')))


    def find_split_rule(self, _id=None):
        url = self.BASE_URL + '/' + str(_id) + '/split_rules'
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            try:
                self.handle_response(json.loads(pagarme_response.content))
            except:
                self.handle_response(json.loads(pagarme_response.content.decode(encoding='UTF-8')))
        else:
            try:
                self.error(pagarme_response.content)
            except:
                self.error(json.loads(pagarme_response.content.decode(encoding='UTF-8')))
            
            