# encoding: utf-8

from pagarme.resources import handler_request
from pagarme.resources.routes import recipient_routes


def create(dictionary):
    return handler_request.post(recipient_routes.BASE_URL, dictionary)


def find_all():
    return handler_request.get(recipient_routes.GET_ALL_RECIPIENTS)


def find_by(search_param):
    return handler_request.get(recipient_routes.GET_RECIPIENT_BY.format(search_param))


def recipient_balance(id_recipient):
    return handler_request.get(recipient_routes.GET_RECIPIENT_BALANCE.format(id_recipient))


def recipient_balance_operation(id_recipient):
    return handler_request.get(recipient_routes.GET_RECIPIENT_BALANCE_OPERATIONS.format(id_recipient))


def recipient_balance_operation_id(id_recipient, operation_id):
    return handler_request.get(recipient_routes.GET_RECIPIENT_BALANCE_OPERATION_BY_ID.format(id_recipient, operation_id))


def update_recipient(id_recipient, update_param):
    return handler_request.put(recipient_routes.UPDATE_RECIPIENT.format(id_recipient), update_param)
