from pagarme.resources.routes.recipient_routes import BASE_URL as BASE_RECIPIENT

BASE_URL = BASE_RECIPIENT + '/{0}/bulk_anticipations'

GET_ALL_ANTICIPATIONS = BASE_URL

GET_ANTICIPATION_LIMITS = BASE_URL + '/limits'
