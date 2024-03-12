from json import dumps
from .requests_retry import requests_retry_session
from .exceptions import GatewayException

TEMPORARY_COMPANY = 'https://api.pagar.me/1/companies/temporary'

KEYS = {}

def validate_response(pagarme_response):
    if pagarme_response.ok:
        return pagarme_response.json()
    else:
        return error(pagarme_response.json())


def create_temporary_company():
    company = requests_retry_session().post(TEMPORARY_COMPANY)
    valid_company = validate_response(company)
    return valid_company


def authentication_key(api_key=None, company_temporary=False):
    global KEYS
    if company_temporary is False:
        KEYS['api_key'] = api_key
        return KEYS
    if company_temporary is True:
        company = create_temporary_company()
        api_key = company['api_key']['test']
        KEYS['api_key'] = api_key
        return KEYS


def delete(end_point, data = {}):
    data['api_key'] = KEYS['api_key']
    pagarme_response = requests_retry_session().delete(end_point, json=data)
    return validate_response(pagarme_response)


def get(end_point, data = {}):
    data['api_key'] = KEYS['api_key']
    pagarme_response = requests_retry_session().get(end_point, json=data)
    return validate_response(pagarme_response)


def post(end_point, data={}):
    data['api_key'] = KEYS['api_key']
    pagarme_response = requests_retry_session().post(end_point, json=data)
    return validate_response(pagarme_response)


def put(end_point, data = {}):
    data['api_key'] = KEYS['api_key']
    pagarme_response = requests_retry_session().put(end_point, json=data)
    return validate_response(pagarme_response)


def error(data):
    raise GatewayException(dumps(data['errors']))
