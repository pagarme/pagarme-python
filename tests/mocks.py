# encoding: utf-8


class FakeResponse(object):
    status_code = 200
    content = '''
        {
            "object": "transaction",
            "status": "processing",
            "refuse_reason": null,
            "status_reason": "acquirer",
            "acquirer_response_code": null,
            "authorization_code": null,
            "soft_descriptor": "testeDeAPI",
            "tid": null,
            "nsu": null,
            "date_created": "2015-02-25T21:54:56.000Z",
            "date_updated": "2015-02-25T21:54:56.000Z",
            "amount": 314,
            "installments": 1,
            "id": 314,
            "cost": 0,
            "postback_url": "",
            "payment_method": "credit_card",
            "antifraud_score": null,
            "boleto_url": null,
            "boleto_barcode": null,
            "boleto_expiration_date": null,
            "referer": "api_key",
            "ip": "189.8.94.42",
            "subscription_id": null,
            "phone": null,
            "address": null,
            "customer": null,
            "card": {
                "object": "card",
                "id": "card_ci6l9fx8f0042rt16rtb477gj",
                "date_created": "2015-02-25T21:54:56.000Z",
                "date_updated": "2015-02-25T21:54:56.000Z",
                "brand": "mastercard",
                "holder_name": "Api Customer",
                "first_digits": "548045",
                "last_digits": "3123",
                "fingerprint": "HSiLJan2nqwn",
                "valid": null
            },
            "metadata": {
                "idProduto": "13933139"
            }
        }
    '''

def fake_request(*args, **kwargs):
    return FakeResponse()

def fake_request_list(*args, **kwargs):
    fakeresponse = FakeResponse()
    fakeresponse.content = '[' + fakeresponse.content + ']'
    return fakeresponse

def fake_request_fail(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"action_forbidden",
        "parameter_name":null,
        "message":"api_key inv\xc3\xa1lida"}],
        "url":"/transactions/314","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_refund(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
        {
            "object": "transaction",
            "status": "refunded",
            "refuse_reason": null,
            "status_reason": "acquirer",
            "acquirer_response_code": null,
            "authorization_code": null,
            "soft_descriptor": "testeDeAPI",
            "tid": null,
            "nsu": null,
            "date_created": "2015-02-25T21:54:56.000Z",
            "date_updated": "2015-02-25T21:54:56.000Z",
            "amount": 314,
            "installments": 1,
            "id": 314,
            "cost": 0,
            "postback_url": "",
            "payment_method": "credit_card",
            "antifraud_score": null,
            "boleto_url": null,
            "boleto_barcode": null,
            "boleto_expiration_date": null,
            "referer": "api_key",
            "ip": "189.8.94.42",
            "subscription_id": null,
            "phone": null,
            "address": null,
            "customer": null,
            "card": {
                "object": "card",
                "id": "card_ci6l9fx8f0042rt16rtb477gj",
                "date_created": "2015-02-25T21:54:56.000Z",
                "date_updated": "2015-02-25T21:54:56.000Z",
                "brand": "mastercard",
                "holder_name": "Api Customer",
                "first_digits": "548045",
                "last_digits": "3123",
                "fingerprint": "HSiLJan2nqwn",
                "valid": null
            },
            "metadata": {
                "idProduto": "13933139"
            }
        }
    """
    return fake

def fake_create_plan(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {
        "object":"plan",
        "id":20112,
        "amount":3100,
        "days":30,
        "name":"nome",
        "trial_days":0,
        "date_created":"2015-09-14T15:02:19.000Z",
        "payment_methods":["boleto",
        "credit_card"],
        "color":null,
        "charges":null,
        "installments":1
    }
    """
    return fake

def fake_get_plan(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {
        "object":"plan",
        "id":20112,
        "amount":3100,
        "days":30,
        "name":"nome",
        "trial_days":0,
        "date_created":"2015-09-14T15:02:19.000Z",
        "payment_methods":["boleto",
        "credit_card"],
        "color":null,
        "charges":null,
        "installments":1
    }
    """
    return fake

def fake_error_plan(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {
        "errors":[{"type":"not_found",
        "parameter_name":null,
        "message":"Plan não encontrado"}],
        "url":"/plans/20234",
        "method":"get"
    }
    """
    fake.status_code = 404
    return fake

def fake_get_sub(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {
        "object": "subscription",
        "plan": {
            "object": "plan",
            "id": 12783,
            "amount": 31000,
            "days": 30,
            "name": "Plano Ouro",
            "trial_days": 0,
            "date_created": "2015-03-03T16:56:32.000Z",
            "payment_methods": ["boleto", "credit_card"],
            "color": null,
            "charges": null,
            "installments": 1
        },
        "id": 16892,
        "current_transaction": {
            "object": "transaction",
            "status": "waiting_payment",
            "refuse_reason": null,
            "status_reason": "acquirer",
            "acquirer_response_code": null,
            "acquirer_name": "development",
            "authorization_code": null,
            "soft_descriptor": null,
            "tid": null,
            "nsu": null,
            "date_created": "2015-04-14T20:17:18.000Z",
            "date_updated": "2015-04-14T20:17:19.000Z",
            "amount": 31000,
            "installments": 1,
            "id": 194402,
            "cost": 0,
            "card_holder_name": null,
            "card_last_digits": null,
            "card_first_digits": null,
            "card_brand": null,
            "postback_url": null,
            "payment_method": "boleto",
            "antifraud_score": null,
            "boleto_url": "https://pagar.me",
            "boleto_barcode": "1234 5678",
            "boleto_expiration_date": "2015-04-21T20:17:18.000Z",
            "referer": "api_key",
            "ip": "179.185.132.108",
            "subscription_id": 16892,
            "metadata": {}
        },
        "postback_url": "http://requestb.in/zyn5obzy",
        "payment_method": "boleto",
        "current_period_start": null,
        "current_period_end": null,
        "charges": 0,
        "status": "unpaid",
        "date_created": "2015-04-14T20:17:19.000Z",
        "phone": null,
        "address": null,
        "customer": {
            "object": "customer",
            "document_number": null,
            "document_type": "cpf",
            "name": null,
            "email": "api@test.com",
            "born_at": null,
            "gender": null,
            "date_created": "2015-03-04T18:40:03.000Z",
            "id": 14437
        },
        "card": null,
        "metadata": null
    }
    """
    return fake

def fake_error_sub(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {
        "errors":[{"type":"not_found",
        "parameter_name":null,
        "message":"Subscription não encontrado"}],
        "url":"/subscriptions/34234",
        "method":"get"
    }
    """
    fake.status_code = 404
    return fake

def fake_card_get(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {
        "object": "card",
        "id": "card_ci6y37h16wrxsmzyi",
        "date_created": "2015-03-06T21:21:25.000Z",
        "date_updated": "2015-03-06T21:21:26.000Z",
        "brand": "visa",
        "holder_name": "API CUSTOMER",
        "first_digits": "401872",
        "last_digits": "8048",
        "fingerprint": "Jl9oOIiDjAjR",
        "customer": null,
        "valid": true
    }
    """
    return fake

def fake_card_error(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {
        "errors": [
            {
                "parameter_name": "card_number",
                "type": "invalid_parameter",
                "message": "Número do cartão está faltando"
            }
        ],
        "url": "/cards",
        "method": "post"
    }
    """
    fake.status_code = 404
    return fake


def fake_bank_accounts_get(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {
        "object": "bank_account",
        "id": 4840,
        "bank_code": "341",
        "agencia": "0932",
        "agencia_dv": "5",
        "conta": "58054",
        "conta_dv": "1",
        "document_type": "cpf",
        "document_number": "26268738888",
        "legal_name": "API BANK ACCOUNT",
        "charge_transfer_fees": false,
        "date_created": "2015-03-19T15:35:40.000Z"
    }
    """
    return fake

def fake_create_recipient(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {
        "object": "recipient",
        "id": "re_ci9bucss300h1zt6dvywufeqc",
        "bank_account": {
            "object": "bank_account",
            "id": 4841,
            "bank_code": "341",
            "agencia": "0932",
            "agencia_dv": "5",
            "conta": "58054",
            "conta_dv": "1",
            "document_type": "cpf",
            "document_number": "26268738888",
            "legal_name": "API BANK ACCOUNT",
            "charge_transfer_fees": false,
            "date_created": "2015-03-19T15:40:51.000Z"
        },
        "transfer_enabled": true,
        "last_transfer": null,
        "transfer_interval": "weekly",
        "transfer_day": 5,
        "automatic_anticipation_enabled": true,
        "anticipatable_volume_percentage": 85,
        "date_created": "2015-05-05T21:41:48.000Z",
        "date_updated": "2015-05-05T21:41:48.000Z"
    }
    """
    return fake

def fake_recipient_get_by_id(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {
        "object": "recipient",
        "id": "re_ci7nhf1ay0007n016wd5t22nl",
        "bank_account": {
            "object": "bank_account",
            "id": 4901,
            "bank_code": "341",
            "agencia": "0932",
            "agencia_dv": null,
            "conta": "58999",
            "conta_dv": "3",
            "document_type": "cpf",
            "document_number": "26268738888",
            "legal_name": "RECIPIENT TEST",
            "charge_transfer_fees": true,
            "date_created": "2015-03-24T15:53:17.000Z"
        },
        "transfer_enabled": true,
        "last_transfer": null,
        "transfer_interval": "weekly",
        "transfer_day": 5,
        "date_created": "2015-03-24T15:53:27.000Z",
        "date_updated": "2015-03-24T15:53:27.000Z"
    }
    """
    return fake



def fake_find_split_rule(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    [{
        "object": "split_rule",
        "id": "sr_ci7ntawl1001s2m164zrbp7tz",
        "recipient_id": "re_ci7nhf1ay0007n016wd5t22nl",
        "charge_processing_fee": true,
        "liable": true,
        "percentage": 30,
        "amount": null,
        "date_created": "2015-03-24T21:26:09.000Z",
        "date_updated": "2015-03-24T21:26:09.000Z"
    }, {
        "object": "split_rule",
        "id": "sr_ci7ntawl1001t2m1606u3e0uw",
        "recipient_id": "re_ci7nheu0m0006n016o5sglg9t",
        "charge_processing_fee": true,
        "liable": false,
        "percentage": 70,
        "amount": null,
        "date_created": "2015-03-24T21:26:09.000Z",
        "date_updated": "2015-03-24T21:26:09.000Z"
    }]
    """
    return fake