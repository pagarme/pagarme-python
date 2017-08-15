from pagarme.resources import handler_request
from pagarme.resources.routes import transfer_routes


def cancel(transfer_id):
    return handler_request.post(transfer_routes.CANCEL_TRANSFER.format(transfer_id))


def create(dictionary):
    return handler_request.post(transfer_routes.BASE_URL, dictionary)


def find_all():
    return handler_request.get(transfer_routes.GET_ALL_TRANSFERS)


def find_by(search_param):
    return handler_request.get(transfer_routes.GET_TRANSFER_BY.format(search_param))
