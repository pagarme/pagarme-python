BASE_URL = 'https://api.pagar.me/1/transactions'

CAPTURE_TRANSACTION_AFTER = BASE_URL + '/{0}/capture'

REFUND_TRANSACTION = BASE_URL + '/{0}/refund'

PAY_BOLETO_NOTIFY = BASE_URL + '/{0}/collect_payment'

PAY_BOLETO = BASE_URL + '/{0}'

CALCULATE_INSTALLMENTS_AMOUNT = BASE_URL + '/calculate_installments_amount'

GENERATE_CARD_HASH_KEY = BASE_URL + '/card_hash_key'

GET_ALL_TRANSACTIONS = BASE_URL

GET_TRANSACTION_BY = BASE_URL + '/{0}'

GET_ALL_PAYABLES_WITH_TRANSACTION_ID = BASE_URL + '/{0}/payables'

GET_SPECIFIC_PAYABLE = BASE_URL + '/{0}/payables/{1}'

GET_TRANSACTION_OPERATION = BASE_URL + '/{0}/operations'

GET_EVENTS_TRANSACTION = BASE_URL + '/{0}/events'

GET_ALL_POSTBACKS = BASE_URL + '/{0}/postbacks'

GET_SPECIFIC_POSTBACK = BASE_URL + '/{0}/postbacks/{1}'

POSTBACK_REDELIVER = BASE_URL + '/{transaction_id}/postbacks/{postback_id}/redeliver'
