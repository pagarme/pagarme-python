from pagarme.resources import handler_request
from pagarme.resources.routes import kyc_link_routes

def create_kyc_link(recipient_id):
    return handler_request.post(kyc_link_routes.CREATE_KYC_LINK(recipient_id))