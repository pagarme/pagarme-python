from tests.resources.dictionaries import transaction_dictionary
from tests.resources.dictionaries import transfer_dictionary
from pagarme import balance_operation
from pagarme import transaction
from pagarme import transfer


def test_find_all_customers():
    boleto = transaction.create(transaction_dictionary.BOLETO_TRANSACTION_SPLIT_RULE_PERCENTAGE)
    transaction.pay_boleto(boleto['id'], transaction_dictionary.PAY_BOLETO)
    transfer_dictionary.TRANSFER_DICTIONARY['recipient_id'] = \
        transaction_dictionary.BOLETO_TRANSACTION_SPLIT_RULE_PERCENTAGE['split_rules'][0]['recipient_id']
    transfer.create(transfer_dictionary.TRANSFER_DICTIONARY)
    balance_operations = balance_operation.find_all()
    assert balance_operations is not None


def test_find_by():
    find_all = balance_operation.find_all()
    find_balance_operation = balance_operation.find_by(find_all[0]['id'])
    assert find_balance_operation['id'] == find_all[0]['id']
