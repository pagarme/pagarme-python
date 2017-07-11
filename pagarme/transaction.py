# encoding: utf-8

from resources import API_KEY as API_KEY
from resources.handler_request import *
from resources.routes.transaction_routes import *

def find_all (api_key):
    return get(BASE_URL,api_key)

def find_by(search_param,api_key):
    return get(GET_TRANSACTION_BY.format(search_param),api_key)

def payables (transaction_id,api_key):
    return get(GET_ALL_PAYABLES_WITH_TRANSACTION_ID.format(transaction_id),api_key)

def operations (transaction_id,api_key):
    return get(GET_TRANSACTION_OPERATION.format(transaction_id),api_key)

def events (transaction_id,api_key):
    return get(GET_EVENTS_TRANSACTION.format(transaction_id),api_key)

def create(dictionary):
	return post(BASE_URL,dictionary)

def capture (transaction_id, dictionary):
    return post(CAPTURE_TRANSACTION_AFTER.format(transaction_id), dictionary)

def refund (transaction_id, dictionary):
    return post(REFUND_TRANSACTION.format(transaction_id),dictionary)
