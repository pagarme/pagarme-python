import requests

from .exceptions import PagarmeApiError

def post (end_point, data):
    pagarme_response = requests.post(end_point,data)
    if pagarme_response.status_code == 200:
        return pagarme_response.json()
    else:
        return error(pagarme_response.json())

def get (end_point, data):
    pagarme_response = requests.get(end_point,data)
    if pagarme_response.status_code == 200:
        return pagarme_response.json()
    else:
        return error(pagarme_response.json())

def put (end_point, data):
    pagarme_response = requests.put(end_point,data)
    if pagarme_response.status_code == 200:
        return pagarme_response.json()
    else:
        return error(pagarme_response.json())

def delete (end_point,data):
    pagarme_response = requests.delete(end_point,data)
    if pagarme_response.status_code == 200:
        return pagarme_response.json()
    else:
        return error(pagarme_response.json())

def error(data):
    e = data['errors'][0]
    error_string = e['type'] + ' - ' + e['message']
    raise PagarmeApiError(error_string)