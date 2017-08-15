from tests.resources.dictionaries import recipient_dictionary
from pagarme import recipient


def test_create_recipient():
    _recipient = recipient.create(recipient_dictionary.RECIPIENT_DICTIONARY)
    assert _recipient['id'] is not None


def test_find_all_recipients():
    all_recipients = recipient.find_all()
    assert all_recipients is not None


def test_find_by():
    _recipient = recipient.create(recipient_dictionary.RECIPIENT_DICTIONARY)
    find_recipient = recipient.find_by(_recipient['id'])
    assert _recipient['id'] == find_recipient['id']


def test_recipient_balance():
    _recipient = recipient.create(recipient_dictionary.RECIPIENT_DICTIONARY)
    recipient_balance = recipient.recipient_balance(_recipient['id'])
    assert recipient_balance['object'] == 'balance'
    assert recipient_balance['available']['amount'] == 0
    assert recipient_balance['waiting_funds']['amount'] == 0
    assert recipient_balance['transferred']['amount'] == 0


def test_recipient_balance_operation():
    _recipient = recipient.create(recipient_dictionary.RECIPIENT_DICTIONARY)
    recipient_balance_operation = recipient.recipient_balance_operation(_recipient['id'])
    assert recipient_balance_operation is not None


def test_update_recipient():
    _recipient = recipient.create(recipient_dictionary.RECIPIENT_DICTIONARY)
    find_recipient = recipient.find_by(_recipient['id'])
    updated_recipient = recipient.update_recipient(find_recipient['id'], recipient_dictionary.UPDATE_RECIPIENT)
    assert find_recipient['transfer_enabled'] != updated_recipient['transfer_enabled']
