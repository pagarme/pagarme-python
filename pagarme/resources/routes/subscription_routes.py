BASE_URL = 'https://api.pagar.me/1/subscriptions'

GET_SUBSCRIPTION_BY_ID = BASE_URL + '/{subscription_id}'

GET_ALL_SUBSCRIPTIONS = BASE_URL

UPDATE_SUBSCRIPTION = BASE_URL + '/{subscription_id}'

CANCEL_SUBSCRIPTION = BASE_URL + '/{subscription_id}/cancel'

SETTLE_CHARGES_SUBSCRIPTION = BASE_URL + '/{subscription_id}/settle_charges'

GET_ALL_SUBSCRIPTIONS_TRANSACTIONS = BASE_URL + '/{subscription_id}/transactions'

GET_ALL_SUBSCRIPTIONS_POSTBACKS = BASE_URL + '/{subscription_id}/postbacks'

GET_SUBSCRIPTION_POSTBACK_BY_ID = BASE_URL + '/{subscription_id}/postbacks/{postback_id}'

REDELIVER_SUBSCRIPTION_POSTBACK_BY_ID = BASE_URL + '/{subscription_id}/postbacks/{postback_id}/redeliver'