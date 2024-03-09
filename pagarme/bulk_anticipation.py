from pagarme.resources import handler_request
from pagarme.resources.routes import bulk_anticipation_routes

def find_all(recipient_id):
    return handler_request.get(bulk_anticipation_routes.GET_ALL_ANTICIPATIONS.format(recipient_id))

def limits(recipient_id, dictionary):
    return handler_request.get(bulk_anticipation_routes.GET_ANTICIPATION_LIMITS.format(recipient_id), dictionary)
