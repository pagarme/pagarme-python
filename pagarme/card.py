from pagarme.resources import handler_request
from pagarme.resources.routes import card_routes


def create(dictionary):
    return handler_request.post(card_routes.BASE_URL, dictionary)


def find_all():
    return handler_request.get(card_routes.GET_ALL_CARDS)


def find_by(param):
    return handler_request.get(card_routes.GET_CARD_BY_ID.format(param))

