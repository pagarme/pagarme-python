from datetime import datetime, timedelta
from pagarme.resources import handler_request
import time


AUTH_TEST = handler_request.authentication_key(None, True)

POSTBACK_URL = 'http://teste.url.com'


def create_postback_url():
    return POSTBACK_URL


def generate_timestamp():
    return int(time.mktime((datetime.now()+timedelta(days=3)).timetuple()) * 1000)
