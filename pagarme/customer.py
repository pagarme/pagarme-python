from pagarme.resources import handler_request
from pagarme.resources.routes import customer_routes


def create(dictionary):
    return handler_request.post(customer_routes.BASE_URL, dictionary)


def find_all():
    return handler_request.get(customer_routes.GET_ALL_CUSTOMERS)


def find_by(search_param):
    return handler_request.get(customer_routes.GET_CUSTOMER_BY.format(search_param))