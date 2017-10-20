import rsa

from pagarme.resources import handler_request
from pagarme.resources.routes import card_routes

from base64 import b64encode
from urllib.parse import urlencode, quote


def create(dictionary):
    return handler_request.post(card_routes.BASE_URL, dictionary)


def find_all():
    return handler_request.get(card_routes.GET_ALL_CARDS)


def find_by(search_params):
    return handler_request.get(card_routes.GET_CARD_BY, search_params)


def hash(request_id, encryption_key, card):
    public_key = rsa.PublicKey.load_pkcs1_openssl_pem(encryption_key)
    encoded_card_data = urlencode(card, quote_via=quote).encode('utf-8')
    encrypted_card_data = rsa.encrypt(encoded_card_data, public_key)
    base64_card_data = b64encode(encrypted_card_data)

    return '{}_{}'.format(request_id, str(base64_card_data.decode('utf-8')))

