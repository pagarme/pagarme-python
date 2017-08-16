from pagarme.resources import handler_request
from pagarme.resources.routes import subscription_routes


def cancel(param):
    return handler_request.post(subscription_routes.CANCEL_SUBSCRIPTION.format(param))


def create(params):
    return handler_request.post(subscription_routes.BASE_URL, params)


def find_all():
    return handler_request.get(subscription_routes.GET_ALL_SUBSCRIPTIONS)


def find_by(param):
    return handler_request.get(subscription_routes.GET_SUBSCRIPTION_BY_ID.format(param))


def transactions(subscription_id):
    return handler_request.get(subscription_routes.GET_ALL_SUBSCRIPTIONS_TRANSACTIONS.format(subscription_id))

def postbacks(subscription_id):
    return handler_request.get(subscription_routes.GET_ALL_SUBSCRIPTIONS_POSTBACKS.format(subscription_id))


def settle_charges(subscription_id, params = {}):
    return handler_request.post(subscription_routes.SETTLE_CHARGES_SUBSCRIPTION.format(subscription_id), params)


def update(subscription_id, params):
    return handler_request.put(subscription_routes.UPDATE_SUBSCRIPTION.format(subscription_id), params)
