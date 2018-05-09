import binascii
import hmac
import re
from hashlib import sha1
from pagarme.resources.handler_request import KEYS


def validate(signature, payload, api_key=None):
    if api_key is None:
        key = KEYS['api_key'] if 'api_key' in KEYS else None
    else:
        key = api_key

    signature = re.sub('sha1=', '', signature)
    payload = payload.encode('utf-8')

    if key not in(None, ''):
        hashed = hmac.new(key.encode(), payload, sha1)
        hex_signature = binascii.b2a_hex(hashed.digest())
        generated_signature = hex_signature.decode()
    else:
        raise Exception('Missing api_key.')

    return generated_signature == signature
