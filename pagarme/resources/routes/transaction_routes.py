BASE_URL = 'https://api.pagar.me/1/transactions'

CAPTURE_TRANSACTION_AFTER = BASE_URL + '/{transaction_id}/capture'

REFUND_TRANSACTION = BASE_URL + '/{transaction_id}/refund'

PAY_BOLETO_NOTIFY = BASE_URL + '/{transaction_id}/collect_payment'

PAY_BOLETO = BASE_URL + '/{transaction_id}'

CALCULETE_INSTALLMENTS = BASE_URL + '/calculate_installments_amount'

GENERATE_ENCRYPTION_KEY_CARD_HASH = BASE_URL + '/transactions/card_hash_key'

GET_ALL_TRANSACTIONS = BASE_URL

GET_TRANSACTION_BY_ID = BASE_URL + '/{transaction_id}'

GET_ALL_PAYABLES_WITH_TRANSACTION_ID = BASE_URL + '/{transaction_id}/payables'

GET_SPECIFIC_PAYABLE = BASE_URL + '/{transaction_id}/payables/{payable_id}'

GET_TRANSACTION_OPERATION = BASE_URL + '/{transaction_id}/operations'

GET_EVENTS_TRANSACTION = BASE_URL + '/{transaction_id}/events'

GET_ALL_TRANSACTIONS_POSTBACKS = BASE_URL + '/{transaction_id}/postbacks'

GET_TRANSACTION_POSTBACK_BY_ID = BASE_URL + '/{transaction_id}/postbacks/{postback_id}'

REDELIVER_TRANSACTION_POSTBACK_BY_ID = BASE_URL + '/{transaction_id}/postbacks/{postback_id}/redeliver'