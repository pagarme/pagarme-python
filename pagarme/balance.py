from pagarme.resources import handler_request
from pagarme.resources.routes import balance_routes


def default_recipeint_balance():
    return handler_request.get(balance_routes.BASE_URL)
