from pagarme.resources import handler_request
from pagarme.resources.routes import transaction_routes


def calculate_installments_amount(dictionary):
    return handler_request.get(transaction_routes.CALCULATE_INSTALLMENTS_AMOUNT, dictionary)


def capture(transaction_id, dictionary):
    return handler_request.post(transaction_routes.CAPTURE_TRANSACTION_AFTER.format(transaction_id), dictionary)


def create(dictionary):
    return handler_request.post(transaction_routes.BASE_URL, dictionary)


def events(transaction_id):
    return handler_request.get(transaction_routes.GET_EVENTS_TRANSACTION.format(transaction_id))


def find_all():
    return handler_request.get(transaction_routes.BASE_URL)


def find_by(search_params):
    return handler_request.get(transaction_routes.GET_TRANSACTION_BY, search_params)


def find_by_id(transaction_id):
    return handler_request.get(transaction_routes.GET_SPECIFIC_TRANSACTION_BY_ID.format(transaction_id))


def generate_card_hash_key():
    return handler_request.get(transaction_routes.GENERATE_CARD_HASH_KEY)


def operations(transaction_id):
    return handler_request.get(transaction_routes.GET_TRANSACTION_OPERATION.format(transaction_id))


def pay_boleto(transaction_id, dictionary):
    return handler_request.put(transaction_routes.PAY_BOLETO.format(transaction_id), dictionary)


# def pay_boleto_notify(dictionary):
#    return handler_request.post(transaction_routes.PAY_BOLETO_NOTIFY,dictionary)


def payables(transaction_id):
    return handler_request.get(transaction_routes.GET_ALL_PAYABLES_WITH_TRANSACTION_ID.format(transaction_id))


def postbacks(transaction_id):
    return handler_request.get(transaction_routes.GET_ALL_POSTBACKS.format(transaction_id))


def postback_redeliver(transaction_id, postback_id):
    return handler_request.post(transaction_routes.POSTBACK_REDELIVER.format(transaction_id, postback_id))


def refund(transaction_id, dictionary):
    return handler_request.post(transaction_routes.REFUND_TRANSACTION.format(transaction_id), dictionary)


def specific_payable(transaction_id, payable_id):
    return handler_request.get(transaction_routes.GET_SPECIFIC_PAYABLE.format(transaction_id, payable_id))


def specific_postback(transaction_id, postback_id):
    return handler_request.get(transaction_routes.GET_SPECIFIC_POSTBACK.format(transaction_id, postback_id))
