import requests

TEMPORARY_COMPANY = 'https://api.pagar.me/1/companies/temporary'


def validate_response(pagarme_response):
    if pagarme_response.status_code == 200:
        return pagarme_response.json()
    else:
        return error(pagarme_response.json())


def create_temporary_company():
    company = requests.post(TEMPORARY_COMPANY)
    valid_company = validate_response(company)
    return valid_company

KEYS ={}

def authentication_key(api_key=None):
    global KEYS
    if api_key is None:
        company = create_temporary_company()
        api_key = company['api_key']['test']
        encryption_key = company['encryption_key']['test']
        KEYS['api_key'] = api_key
        KEYS['encryption_key'] = encryption_key
        return KEYS
    else:
        KEYS['api_key'] = api_key
        return KEYS


def post(end_point, data={}):
    data['api_key'] = KEYS['api_key']
    pagarme_response = requests.post(end_point, data)
    return validate_response(pagarme_response)


def get(end_point, data={}):
    data['api_key'] = KEYS['api_key']
    pagarme_response = requests.get(end_point, data)
    return validate_response(pagarme_response)


def put(end_point, data={}):
    data['api_key'] = KEYS['api_key']
    pagarme_response = requests.put(end_point, data)
    return validate_response(pagarme_response)


def delete(end_point, data={}):
    data['api_key'] = KEYS['api_key']
    pagarme_response = requests.delete(end_point, data)
    return validate_response(pagarme_response)


def error(data):
    erros = data['errors']
    return erros
