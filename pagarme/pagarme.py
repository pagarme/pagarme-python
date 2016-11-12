# encoding: utf-8
import hashlib
import json
import requests

from .card import Card
from .exceptions import PagarmeApiError
from .subscription import Plan, Subscription
from .transaction import Transaction


class Pagarme(object):
    def __init__(self, api_key=None):
        if not api_key:
            raise ValueError('You should suply the api key.')
        self.api_key = api_key

    def start_transaction(
            self,
            amount=None,
            card_hash=None,
            card_id=None,
            payment_method='credit_card',
            installments=1,
            postback_url=None,
            **kwargs):

        if not amount:
            raise ValueError('You should suply the value')
        if payment_method == 'credit_card' and not (card_id or card_hash):
            raise ValueError('You should suply a card_hash or card_id')
        if payment_method not in ('credit_card', 'boleto'):
            raise ValueError('Invalid payment_method')
        if not installments:
            raise ValueError('Invalid installments')

        return Transaction(
            api_key=self.api_key,
            amount=amount,
            card_hash=card_hash,
            card_id=card_id,
            payment_method=payment_method,
            installments=installments,
            postback_url=postback_url,
            **kwargs)

    def error(self, data):
        e = data['errors'][0]
        error_string = e['type'] + ' - ' + e['message']
        raise PagarmeApiError(error_string)

    def find_transaction_by_id(self, id):
        transaction = Transaction(api_key=self.api_key)
        transaction.find_by_id(id)
        return transaction

    def all_transactions(self, page=1, count=10):
        return self.get_all_resources(Transaction, page, count)

    def validate_fingerprint(self, object_id, fingerprint):
        code = str(object_id) + '#' + self.api_key
        code = code.encode('utf-8')
        sha1_hash = hashlib.sha1(code).hexdigest()
        return fingerprint == sha1_hash

    def start_plan(
            self,
            name,
            amount=None,
            days=None,
            payment_methods=['boleto', 'credit_card'],
            color=None,
            charges=1,
            installments=1,
            trial_days=0,
            **kwargs):

        if not isinstance(amount, int):
            raise ValueError('Amount should be an int')
        if days is None:
            raise ValueError('Missing days')

        plan = Plan(
            api_key=self.api_key,
            amount=amount,
            name=name,
            days=days,
            installments=installments,
            payment_methods=payment_methods,
            color=color,
            charges=charges,
            trial_days=trial_days,
            **kwargs)

        return plan

    def find_plan_by_id(self, id):
        plan = Plan(self.api_key)
        plan.find_by_id(id)
        return plan

    def all_plans(self, page=1, count=10):
        return self.get_all_resources(Plan, page, count)

    def start_subscription(
            self,
            plan_id=None,
            plan=None,
            card_id=None,
            card_hash=None,
            postback_url=None,
            customer=None,
            **kwargs):

        if plan_id is None:
            plan_id = plan.data['id']
        sub = Subscription(
            api_key=self.api_key, plan_id=plan_id, card_id=card_id,
            card_hash=card_hash, postback_url=postback_url, customer=customer,
            **kwargs)
        return sub

    def find_subscription_by_id(self, id):
        s = Subscription(self.api_key)
        s.find_by_id(id)
        return s

    def all_subscriptions(self, page=1, count=10):
        return self.get_all_resources(Subscription, page, count)

    def get_all_resources(self, Class, page, count):
        data = {
            'api_key': self.api_key,
            'page': page,
            'count': count,
        }
        url = Class.BASE_URL
        pagarme_response = requests.get(url, params=data)
        if pagarme_response.status_code != 200:
            self.error(pagarme_response.json())
        responses = pagarme_response.json()
        resources = []
        for response in responses:
            resource = Class(api_key=self.api_key)
            resource.handle_response(response)
            resources.append(resource)
        return resources

    def find_card_by_id(self, id=None):
        card = Card(self.api_key)
        card.find_by_id(id)
        return card
