from pagarme import transaction
from pagarme import kyc_link
from pagarme import recipient
from tests.resources.dictionaries import transaction_dictionary
from tests.resources.dictionaries import recipient_dictionary


def test_create_kyc_link():
    transaction.create(transaction_dictionary.VALID_CREDIT_CARD_TRANSACTION)
    default_recipient_id = transaction_dictionary.DEFAULT_RECIPIENT
    recipient.update_recipient(default_recipient_id, recipient_dictionary.UPDATE_RECIPIENT)
    _kyc_link = kyc_link.create_kyc_link(default_recipient_id)
    assert _kyc_link is not None