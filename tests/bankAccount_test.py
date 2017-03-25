import mock

from .mocksBankAccount import fake_request,fake_request_fail_id,fake_request_fail_bank_code,fake_request_fail_agencia
from .mocksBankAccount import fake_request_fail_agencia_dv,fake_request_fail_conta,fake_request_fail_conta_dv
from .mocksBankAccount import fake_request_fail_type, fake_request_fail_document_number,fake_request_fail_legal_name
from pagarme.bankAccount import BankAccount,PagarmeApiError
from .pagarme_test import PagarmeTestCase


class BankAccountTestCase(PagarmeTestCase):

    @mock.patch('requests.post', mock.Mock(side_effect=fake_request))
    def test_create_bankAccount(self):
        bankAccount = BankAccount(api_key='apikey', bank_code='341', agencia='3209', agencia_dv='4', conta='58054', conta_dv='1',
            type='conta_corrente',document_number='26268738888',legal_name='BANK ACCOUNT PYTHON"')
        bankAccount.charge()
        self.assertEqual('26268738888',bankAccount.document_number)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_bankAccount_by_id(self):
        bankAccount = BankAccount(api_key='apikey')
        bankAccount.find_by_id(17422412)
        self.assertEqual(17422412, bankAccount.id)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_id))
    def test_get_bankAccount_by_id_fail(self):
        bankAccount = BankAccount(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            bankAccount.find_by_id(17422412)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_bankAccount_by_bank_code(self):
        bankAccount = BankAccount(api_key='apikey')
        bankAccount.find_by_bank_code(341)
        self.assertEqual('341', bankAccount.bank_code)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_bank_code))
    def test_get_bankAccount_by_bank_code_fail(self):
        bankAccount = BankAccount(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            bankAccount.find_by_bank_code(341)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_bankAccount_by_agencia(self):
        bankAccount = BankAccount(api_key='apikey')
        bankAccount.find_by_agencia(3209)
        self.assertEqual('3209', bankAccount.agencia)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_agencia))
    def test_get_bankAccount_by_agencia_fail(self):
        bankAccount = BankAccount(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            bankAccount.find_by_agencia(3209)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_bankAccount_by_agencia_dv(self):
        bankAccount = BankAccount(api_key='apikey')
        bankAccount.find_by_agencia_dv(5)
        self.assertEqual('5', bankAccount.agencia_dv)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_agencia_dv))
    def test_get_bankAccount_by_agencia_dv_fail(self):
        bankAccount = BankAccount(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            bankAccount.find_by_agencia_dv(5)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_bankAccount_by_conta(self):
        bankAccount = BankAccount(api_key='apikey')
        bankAccount.find_by_conta(58054)
        self.assertEqual('58054', bankAccount.conta)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_conta))
    def test_get_bankAccount_by_conta_fail(self):
        bankAccount = BankAccount(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            bankAccount.find_by_conta(58054)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_bankAccount_by_conta_dv(self):
        bankAccount = BankAccount(api_key='apikey')
        bankAccount.find_by_conta_dv(1)
        self.assertEqual('1', bankAccount.conta_dv)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_conta_dv))
    def test_get_bankAccount_by_conta_dv_fail(self):
        bankAccount = BankAccount(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            bankAccount.find_by_conta_dv(1)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_bankAccount_by_type(self):
        bankAccount = BankAccount(api_key='apikey')
        bankAccount.find_by_type('conta_corrente')
        self.assertEqual('conta_corrente', bankAccount.type)
            
    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_type))
    def test_get_bankAccount_by_type_fail(self):
        bankAccount = BankAccount(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            bankAccount.find_by_type('conta_corrente')

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_bankAccount_by_document_number(self):
        bankAccount = BankAccount(api_key='apikey')
        bankAccount.find_by_document_number(26268738888)
        self.assertEqual('26268738888', bankAccount.document_number)
            
    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_document_number))
    def test_get_bankAccount_by_document_number_fail(self):
        bankAccount = BankAccount(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            bankAccount.find_by_document_number(26268738888)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_bankAccount_by_legal_name(self):
        bankAccount = BankAccount(api_key='apikey')
        bankAccount.find_by_legal_name('BANK ACCOUNT PYTHON')
        self.assertEqual('BANK ACCOUNT PYTHON', bankAccount.legal_name)
            
    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail_legal_name))
    def test_get_bankAccount_by_legal_name_fail(self):
        bankAccount = BankAccount(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            bankAccount.find_by_legal_name('BANK ACCOUNT PYTHON')