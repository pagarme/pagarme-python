from tests.resources.dictionaries import payable_dictionary
from pagarme import payable


def test_find_all_payables():
    all_payables = payable.find_all()
    print(all_payables)
    assert all_payables is not None


def test_find_by():
    find_payable = payable.find_by(payable_dictionary.PAYABLES[0]['id'])
    assert find_payable['id'] is not None
