BASE_URL = 'https://api.pagar.me/1/transactions'

CAPTURE_TRANSACTION_AFTER = BASE_URL + '/{0}/capture'

REFUND_TRANSACTION = BASE_URL + '/{0}/refund'

PAY_BOLETO_NOTIFY = BASE_URL + '/{transaction_id}/collect_payment'

PAY_BOLETO = BASE_URL + '/{transaction_id}'

CALCULETE_INSTALLMENTS = BASE_URL + '/calculate_installments_amount'

GENERATE_ENCRYPTION_KEY_CARD_HASH = BASE_URL + '/transactions/card_hash_key'

GET_ALL_TRANSACTIONS = BASE_URL

GET_TRANSACTION_BY = BASE_URL + '/{0}'

GET_ALL_PAYABLES_WITH_TRANSACTION_ID = BASE_URL + '/{0}/payables'

GET_SPECIFIC_PAYABLE = BASE_URL + '/{transaction_id}/payables/{payable_id}'

GET_TRANSACTION_OPERATION = BASE_URL + '/{0}/operations'

GET_EVENTS_TRANSACTION = BASE_URL + '/{0}/events'