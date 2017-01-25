# encoding: utf-8

import mock

from pagarme import Customer
from pagarme.transaction import Transaction, PagarmeApiError, NotPaidException, NotBoundException

from .mocks import fake_request, fake_request_fail, fake_request_refund, fake_request_partial_capture
from .pagarme_test import PagarmeTestCase


class TransactionTestCase(PagarmeTestCase):

    @mock.patch('requests.post', mock.Mock(side_effect=fake_request))
    def test_charge(self):
        transaction = Transaction(api_key='apikey', amount=314, card_hash='foobar', payment_method='credit_card', installments=1, postback_url='https://post.back.url')
        transaction.charge()
        self.assertEqual('processing', transaction.status)

    @mock.patch('requests.post', mock.Mock(side_effect=fake_request_fail))
    def test_charge_fail(self):
        transaction = Transaction(api_key='apikey', amount=314, card_hash='foobar', payment_method='credit_card', installments=1, postback_url='https://post.back.url')
        with self.assertRaises(PagarmeApiError):
            transaction.charge()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_transaction_by_id(self):
        transaction = Transaction(api_key='apikey')
        transaction.find_by_id(314)
        self.assertEqual(314, transaction.id)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail))
    def test_get_transaction_by_id_fails(self):
        transaction = Transaction(api_key='apikey')
        with self.assertRaises(PagarmeApiError):
            transaction.find_by_id(314)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    @mock.patch('requests.post', mock.Mock(side_effect=fake_request_refund))
    def test_refund_transaction(self):
        transaction = Transaction(api_key='apikey')
        transaction.find_by_id(314)
        transaction.refund()
        self.assertEqual('refunded', transaction.status)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    @mock.patch('requests.post', mock.Mock(side_effect=fake_request_partial_capture))
    def test_partial_capture(self):
        transaction = Transaction(api_key='apikey')
        transaction.find_by_id(1122193)
        transaction.amount = 5000
        transaction.capture()
        self.assertEqual(5000,transaction.paid_amount)
                

    def test_refund_transaction_before_set_id(self):
        transaction = Transaction(api_key='apikey')
        with self.assertRaises(NotPaidException):
            transaction.refund()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    @mock.patch('requests.post', mock.Mock(side_effect=fake_request_fail))
    def test_refund_transaction_fail(self):
        transaction = Transaction(api_key='apikey')
        transaction.find_by_id(314)
        with self.assertRaises(PagarmeApiError):
            transaction.refund()

    def test_metadata_is_sended_(self):
        transaction = Transaction(
            api_key='apikey',
            amount=314,
            card_hash='cardhash',
            metadata={'sku': 'foo bar'},
        )
        self.assertEqual('foo bar', transaction.get_data()['metadata[sku]'])

    def test_transaction_can_have_any_arguments(self):
        transaction = Transaction(
            api_key='apikey',
            amount=314,
            card_hash='cardhash',
            any_argument='any_value',
        )
        self.assertIn('any_argument', transaction.get_data())

    @mock.patch('requests.post', mock.Mock(side_effect=fake_request))
    def test_transaction_capture_later(self):
        transaction = Transaction(
            api_key='apikey',
            amount=314,
            card_hash='cardhash',
            capture=False,
        )
        transaction.charge()
        transaction.capture()

    @mock.patch('requests.post', mock.Mock(side_effect=fake_request_fail))
    def test_transaction_capture_later_without_charger(self):
        transaction = Transaction(
            api_key='apikey',
            amount=314,
            card_hash='cardhash',
            capture=False,
        )
        with self.assertRaises(NotBoundException):
            transaction.capture()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    @mock.patch('requests.post', mock.Mock(side_effect=fake_request_fail))
    def test_transaction_capture_later_fails(self):
        transaction = Transaction(api_key='apikey')
        transaction.find_by_id(314)
        with self.assertRaises(PagarmeApiError):
            transaction.capture()

    @mock.patch('requests.post', mock.Mock(side_effect=fake_request))
    def test_transaction_with_ant_fraud(self):
        customer = Customer(
            name='foo bar',
            document_number='11122233345',
            email='teste@email.com.br',
            address_street='bar foo',
            address_neighborhood='baz for',
            address_zipcode='3945154',
            address_street_number='99',
            phone_ddd='31',
            phone_number='9144587'
        )

        transaction = Transaction(
            api_key='apikey',
            amount=314,
            card_hash='cardhash',
            customer = customer
        )
        self.assertIn('customer[phone][ddd]', transaction.get_data())

    @mock.patch('requests.post', mock.Mock(side_effect=fake_request_fail))
    def test_charge_transaction_with_invalid_split_rules_fails(self):
        transaction = Transaction(
            apikey='apikey',
            amount=10000,
            payment_method='boleto',
            split_rules = [
                {
                    "recipient_id":"idrecipient",
                    "liable":"true",
                    "charge_processing_fee":"true",
                    "percentage":"80" 
                },
                {
                    "recipient_id":"idrecipient",
                    "liable":"true",
                    "charge_processing_fee":"true",
                    "percentage":"30"
                }
            ]
        )
        with self.assertRaises(PagarmeApiError):
            transaction.charge()
 
    @mock.patch('requests.post', mock.Mock(side_effect=fake_request))
    def test_charge_transaction_with_valid_split_rules(self):
        transaction = Transaction(
            apikey='apikey',
            amount=10000,
            payment_method='boleto',
            split_rules = [
                {
                    "recipient_id":"idrecipient",
                    "liable":"true",
                    "charge_processing_fee":"true",
                    "percentage":"20"
                },
                {
                    "recipient_id":"idrecipient2",
                    "liable":"true",
                    "charge_processing_fee":"true",
                    "percentage":"80"
                }
            ]
        )
        transaction.charge()
        self.assertEqual('processing',transaction.status)
