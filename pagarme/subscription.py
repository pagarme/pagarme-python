# encoding: utf-8

import requests

from .exceptions import NotBoundException
from .resource import AbstractResource
from .settings import BASE_URL
from .transaction import Transaction


class Plan(AbstractResource):
    BASE_URL = BASE_URL + 'plans'

    def __init__(self, api_key='', name='', amount=None, days=None, installments=1, payment_methods=['boleto', 'credit_card'],
                 color=None, charges=1, trial_days=0, **kwargs):

        if not api_key:
            raise ValueError('You should supply an api_key')
        for payment_method in payment_methods:
            if payment_method not in ['boleto', 'credit_card']:
                raise ValueError('Invalid payment method, try a list with "boleto" and/or "credit_card"')

        self.data = {'api_key': api_key}
        self.data['name'] = name
        self.data['amount'] = amount
        self.data['installments'] = installments
        self.data['payment_methods'] = payment_methods
        self.data['color'] = color
        self.data['charges'] = charges
        self.data['trial_days'] = trial_days
        self.data['days'] = days

        self.data.update(kwargs)

    def find_by_id(self, id):
        url = self.BASE_URL + '/' + str(id)
        data = {'api_key': self.data['api_key']}
        pagarme_response = requests.get(url, params=data)
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())


class Subscription(AbstractResource):
    BASE_URL = BASE_URL + 'subscriptions'

    def __init__(
            self,
            api_key=None,
            plan_id=None,
            card_id=None,
            card_hash=None,
            postback_url=None,
            metadata={},
            customer=None,
            **kwargs):
        if not api_key:
            raise ValueError('Invalid api_key')
        if plan_id and not isinstance(plan_id, int):
            raise ValueError('plan_id should be a int')
        if customer and not customer.data['email']:
            raise ValueError('Customer email not found')

        self.data = {
            'api_key': api_key,
            'plan_id': plan_id,
            'card_hash': card_hash,
            'postback_url': postback_url,
        }
        self.metadata = metadata
        self.customer = customer

        if card_hash:
            self.data['card_hash'] = card_hash
        else:
            self.data['card_id'] = card_id

        self.data.update(kwargs)

    def get_data(self):
        data = self.data
        if self.customer:
            data.update(self.customer.get_anti_fraud_data())
        if self.metadata:
            for key, value in self.metadata.items():
                new_key = 'metadata[{key}]'.format(key=key)
                data[new_key] = value
        return data

    def find_by_id(self, id):
        url = self.BASE_URL + '/' + str(id)
        data = {'api_key': self.data['api_key']}
        pagarme_response = requests.get(url, params=data)
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def cancel(self):
        if not self.data.get('id', False):
            raise NotBoundException('First try search your subscription')
        url = self.BASE_URL + '/{id}/cancel'.format(id=self.data['id'])
        pagarme_response = requests.post(url, data={'api_key': self.data['api_key']})
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def transactions(self):
        if not self.data.get('id', False):
            raise NotBoundException('First try search your subscription')
        url = self.BASE_URL + '/{id}/transactions'.format(id=self.data['id'])
        pagarme_response = requests.get(url, params={'api_key': self.data['api_key']})
        if pagarme_response.status_code != 200:
            self.error(pagarme_response.json())
        response = pagarme_response.json()
        transactions = []
        for transaction in response:
            t = Transaction(self.data['api_key'])
            t.handle_response(transaction)
            transactions.append(t)
        return transactions
