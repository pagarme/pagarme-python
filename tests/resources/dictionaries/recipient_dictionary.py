from pagarme import bank_account
from tests.resources.dictionaries import bank_account_dictionary

BANK_ACCOUNT = bank_account.create(bank_account_dictionary.BANK_ACCOUNT)

RECIPIENT = {
    'anticipatable_volume_percentage': '80',
    'automatic_anticipation_enabled': 'true',
    'transfer_day': '5',
    'transfer_enabled': 'true',
    'transfer_interval': 'weekly',
    'bank_account_id': BANK_ACCOUNT['id']
}

UPDATE_RECIPIENT = {
    'transfer_enabled': 'false',
    'anticipatable_volume_percentage': '85'
}

REGISTER_INFORMATION = {
    'type': 'individual',
    'document_number': '12345678910',
    'name': 'Someone',
    'site_url': '',
    'email': 'some',
    'mother_name': 'Eliana',
    'birthdate': '01',
    'monthly_income': '1000',
    'professional_occupation': 'Empresário',
    'address': {
        'street': None,
        'complementary': 'SN',
        'street_number': None,
        'neighborhood': None,
        'city': None,
        'state': None,
        'zipcode': None,
        'reference_point': None
  },
  'phone_numbers': [
    {
      'ddd': '27',
      'number': '999992628',
      'type': 'primary'
    }
  ]
}