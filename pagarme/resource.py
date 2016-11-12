# encoding: utf-8

import requests

from .exceptions import PagarmeApiError


class AbstractResource(object):
    def __init__(self):
        raise NotImplementedError

    def handle_response(self, data):
        self.data.update(data)

    def error(self, data):
        e = data['errors'][0]
        error_string = e['type'] + ' - ' + e['message']
        raise PagarmeApiError(error_string)

    def create(self):
        url = self.BASE_URL
        pagarme_response = requests.post(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(pagarme_response.json())
        else:
            self.error(pagarme_response.json())

    def get_data(self):
        return self.data
