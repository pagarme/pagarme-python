# encoding: utf-8

import mock

from pagarme.bank_accounts import BankAccount
from pagarme.exceptions import PagarmeApiError

from .pagarme_test import PagarmeTestCase
from .mocks import fake_bank_accounts_get


class BankAccountTestCase(PagarmeTestCase):

    @mock.patch('requests.post', mock.Mock(side_effect=fake_bank_accounts_get))
    def test_create_bank_accounts_with_data(self):
        bank_accounts = BankAccount(api_key='api_key', 
                                    bank_code=341, 
                                    agencia=932, 
                                    agencia_dv=5,
                                    conta=58054,
                                    conta_dv=1, 
                                    document_number=26268738888, 
                                    legal_name='API BANK ACCOUNT')
        bank_accounts.create()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_bank_accounts_get))
    def test_find_bank_accounts_by_id(self):
        bank_accounts = BankAccount(api_key='api_key', id=4840)
        bank_accounts.find_by_id()
        self.assertEqual(bank_accounts.data['conta'], '58054')

    def test_find_bank_accounts_by_id_fail(self):
        bank_accounts = BankAccount(api_key='api_key', id=0000)
        with self.assertRaises(PagarmeApiError):
            bank_accounts.find_by_id()

    def test_find_bank_accounts_list(self):
        bank_accounts = BankAccount(api_key='api_key')
        with self.assertRaises(ValueError):
            bank_accounts.find_by_id()
