import requests

from .exceptions import PagarmeApiError, NotBoundException
from .resource import AbstractResource
from .settings import BASE_URL


class BankAccount(AbstractResource):
    BASE_URL = BASE_URL + 'bank_accounts'

    def __init__(
        self,
        api_key=None,
        bank_code=None,
        agencia=None,
        agencia_dv=None,
        conta=None,
        conta_dv=None,
        type=['conta_corrente','conta_poupanca','conta_corrente_conjunta','conta_poupanca_conjunta'],
        document_number=None,
        legal_name=None,
        **kwargs):

        self.api_key = api_key
        self.bank_code = bank_code
        self.agencia = agencia
        self.agencia_dv = agencia_dv
        self.conta = conta
        self.conta_dv = conta_dv
        self.type = type
        self.document_number = document_number
        self.legal_name = legal_name
        self.id = None
        self.data = {}

        for key, value in kwargs.items():
            self.data[key] = value

    def handle_response(self, data):
        self.id = data['id']
        self.bank_code = data['bank_code']
        self.agencia = data['agencia']
        self.agencia_dv = data['agencia_dv']
        self.conta = data['conta']
        self.conta_dv = data['conta_dv']
        self.type = data['type']
        self.document_number = data['document_number']
        self.legal_name = data['legal_name']
    
    def __dict__(self):
        d = self.data
        d['api_key'] = self.api_key
        d['bank_code'] = self.bank_code
        d['agencia'] = self.agencia
        d['agencia_dv'] = self.agencia_dv
        d['conta'] = self.conta
        d['conta_dv'] = self.conta_dv
        d['type'] = self.type
        d['document_number'] = self.document_number
        d['legal_name'] = self.legal_name

        return d

    def get_data(self):
        return self.__dict__()

    def charge(self):
        self.create()

    def find_by_id(self, id=None):
        url = self.BASE_URL + '/' + str(id)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_bank_code(self, bank_code=None):
        url = self.BASE_URL + '/' + str(bank_code)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_agencia(self, agencia=None):
        url = self.BASE_URL + '/' + str(agencia)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_agencia_dv(self, agencia_dv=None):
        url = self.BASE_URL + '/' + str(agencia_dv)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_conta(self, conta=None):
        url = self.BASE_URL + '/' + str(conta)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_conta_dv(self, conta_dv=None):
        url = self.BASE_URL + '/' + str(conta_dv)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_type(self, type=None):
        url = self.BASE_URL + '/' + str(type)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_document_number(self, document_number=None):
        url = self.BASE_URL + '/' + str(document_number)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def find_by_legal_name(self, legal_name=None):
        url = self.BASE_URL + '/' + str(legal_name)
        pagarme_response = requests.get(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())