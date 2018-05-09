from pagarme import customer
from tests.resources.dictionaries import customer_dictionary
import time


def test_create_customer():
    _customer = customer.create(customer_dictionary.CUSTOMER)
    assert _customer['id'] is not None


def test_find_all_customers():
    all_customers = customer.find_all()
    assert all_customers is not None


def test_find_by():
    _customer = customer.create(customer_dictionary.CUSTOMER)
    time.sleep(3)
    search_params = {'id': str(_customer['id'])}
    find_customer = customer.find_by(search_params)
    assert _customer['id'] == find_customer[0]['id']
