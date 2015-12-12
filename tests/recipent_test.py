# encoding: utf-8

import mock

from .pagarme_test import PagarmeTestCase
from pagarme.recipients import Recipient
from tests.mocks import fake_create_recipient, fake_recipient_get_by_id

class RecipientTestCase(PagarmeTestCase):

    @mock.patch('requests.post', mock.Mock(side_effect=fake_create_recipient))
    def test_create_recipient_with_data(self):
        recipient = Recipient(api_key='api_key', 
                                    transfer_interval='daily', 
                                    transfer_day='6',
                                    transfer_enabled='true', 
                                    bank_account_id='9332')
        recipient.create()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_recipient_get_by_id))
    def test_find_recipient_by_id(self):
        recipient = Recipient(api_key='api_key', id='re_cihuw7xc6004t426er5llvqds')
        recipient.find_by_id()
        self.assertEqual(recipient.data['id'], 're_cihuw7xc6004t426er5llvqds')
