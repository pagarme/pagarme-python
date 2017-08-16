from tests.resources.dictionaries import transaction_dictionary
from pagarme import transaction


TRANSACTION = transaction.create(transaction_dictionary.VALID_CREDIT_CARD_TRANSACTION_DICTIONARY)

PAYABLES = transaction.payables(TRANSACTION['id'])
