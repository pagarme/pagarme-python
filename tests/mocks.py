# encoding: utf-8
import json


class FakeResponse(object):
    status_code = 200
    content = '''
        {
            "object": "transaction",
            "status": "processing",
            "refuse_reason": null,
            "status_reason": "acquirer",
            "acquirer_response_code": "0000",
            "acquirer_name": "pagarme",
            "acquirer_id": "57e9762df61cf04a06b75f02",
            "authorization_code": "470029",
            "soft_descriptor": null,
            "tid": 314,
            "nsu": 314,
            "date_created": "2017-01-18T19:40:54.898Z",
            "date_updated": "2017-01-18T19:40:55.328Z",
            "amount": 10000,
            "authorized_amount": 10000,
            "paid_amount": 50000,
            "refunded_amount": 0,
            "installments": 1,
            "id": 314,
            "cost": 50,
            "card_holder_name": " TESTE",
            "card_last_digits": "4242",
            "card_first_digits": "424242",
            "card_brand": "visa",
            "card_pin_mode": null,
            "postback_url": "http://requestb.in/10hnj9t1",
            "payment_method": "credit_card",
            "capture_method": "ecommerce",
            "antifraud_score": null,
            "boleto_url": null,
            "boleto_barcode": null,
            "boleto_expiration_date": null,
            "referer": "api_key",
            "ip": "187.11.121.49",
            "subscription_id": null,
            "phone": {
                "object": "phone",
                "ddi": "55",
                "ddd": "11",
                "number": "50505050",
                "id": 82909
            },
            "address": {
                "object": "address",
                "street": "Avenida das Nações Unidas",
                "complementary": null,
                "street_number": "1000",
                "neighborhood": "Berrini",
                "city": "São Paulo",
                "state": "SP",
                "zipcode": "01215010",
                "country": "Brasil",
                "id": 85267
            },
            "customer": {
                "object": "customer",
                "document_number": "85605046055",
                "document_type": "cpf",
                "name": "Teste",
                "email": "teste@hotmail.com",
                "born_at": null,
                "gender": "M",
                "date_created": "2017-01-17T18:48:39.848Z",
                "id": 140389
            },
            "card": {
                "object": "card",
                "id": "card_cixiw3v52007eqf6ep1drw7u4",
                "date_created": "2017-01-04T11:58:10.027Z",
                "date_updated": "2017-01-04T11:58:10.199Z",
                "brand": "visa",
                "holder_name": " TESTE",
                "first_digits": "424242",
                "last_digits": "4242",
                "country": "US",
                "fingerprint": "PEyFKWzMdB34",
                "valid": true,
                "expiration_date": "0120"
            },
            "split_rules": null,
            "antifraud_metadata": {},
            "metadata": {}
        }
    '''

    def json(self):
        return json.loads(self.content)

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

def fake_request_partial_capture(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
        {
            "object": "transaction",
            "status": "paid",
            "refuse_reason": null,
            "status_reason": "acquirer",
            "acquirer_response_code": "0000",
            "acquirer_name": "pagarme",
            "acquirer_id": "56f9d019decf72cc70055d58",
            "authorization_code": "402918",
            "soft_descriptor": null,
            "tid": 1122193,
            "nsu": 1122193,
            "date_created": "2017-01-19T17:24:48.909Z",
            "date_updated": "2017-01-19T17:25:20.453Z",
            "amount": 10000,
            "authorized_amount": 10000,
            "paid_amount": 5000,
            "refunded_amount": 0,
            "installments": 1,
            "id": 1122193,
            "cost": 50,
            "card_holder_name": "Alex Silva",
            "card_last_digits": "4242",
            "card_first_digits": "424242",
            "card_brand": "visa",
            "card_pin_mode": null,
            "postback_url": "http://requestb.in/14i32g71",
            "payment_method": "credit_card",
            "capture_method": "ecommerce",
            "antifraud_score": null,
            "boleto_url": null,
            "boleto_barcode": null,
            "boleto_expiration_date": null,
            "referer": "api_key",
            "ip": "187.11.121.49",
            "subscription_id": null,
            "phone": {
              "object": "phone",
              "ddi": "55",
              "ddd": "11",
              "number": "99999999",
              "id": 78641
            },
            "address": {
              "object": "address",
              "street": "Avenida Brigadeiro Faria Lima",
              "complementary": null,
              "street_number": "1811",
              "neighborhood": "Jardim Paulistano",
              "city": "São Paulo",
              "state": "SP",
              "zipcode": "01451001",
              "country": "Brasil",
              "id": 81006
            },
            "customer": {
              "object": "customer",
              "document_number": "18152564000105",
              "document_type": "cnpj",
              "name": "John Smith",
              "email": "aardvark.silva@pagar.me",
              "born_at": "1970-01-01T03:38:41.988Z",
              "gender": "M",
              "date_created": "2016-08-05T19:09:27.251Z",
              "id": 85789
            },
            "card": {
              "object": "card",
              "id": "card_ciy33symx0005ky6eoa2k16rh",
              "date_created": "2017-01-18T15:29:01.788Z",
              "date_updated": "2017-01-18T15:29:02.432Z",
              "brand": "visa",
              "holder_name": "Alex Silva",
              "first_digits": "424242",
              "last_digits": "4242",
              "country": "US",
              "fingerprint": "8Z6Lxj449c8M",
              "valid": true,
              "expiration_date": "1119"
            },
            "split_rules": null,
            "metadata": {},
            "antifraud_metadata": {}
        }
    """
    return fake


def fake_request_refund(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
        {
            "object": "transaction",
            "status": "refunded",
            "refuse_reason": null,
            "status_reason": "acquirer",
            "acquirer_response_code": "0000",
            "acquirer_name": "pagarme",
            "acquirer_id": "57e9762df61cf04a06b75f02",
            "authorization_code": "470029",
            "soft_descriptor": null,
            "tid": 314,
            "nsu": 314,
            "date_created": "2017-01-18T19:40:54.898Z",
            "date_updated": "2017-01-25T12:59:17.370Z",
            "amount": 1000,
            "authorized_amount": 100000,
            "paid_amount": 100000,
            "refunded_amount": 100000,
            "installments": 1,
            "id": 314,
            "cost": 0,
            "card_holder_name": " TESTE",
            "card_last_digits": "4242",
            "card_first_digits": "424242",
            "card_brand": "visa",
            "card_pin_mode": null,
            "postback_url": "http://requestb.in/10hnj9t1",
            "payment_method": "credit_card",
            "capture_method": "ecommerce",
            "antifraud_score": null,
            "boleto_url": null,
            "boleto_barcode": null,
            "boleto_expiration_date": null,
            "referer": "api_key",
            "ip": "187.11.121.49",
            "subscription_id": null,
            "phone": {
                "object": "phone",
                "ddi": "55",
                "ddd": "11",
                "number": "50505050",
                "id": 82909
            },
            "address": {
                "object": "address",
                "street": "Avenida das Nações Unidas",
                "complementary": null,
                "street_number": "1000",
                "neighborhood": "Berrini",
                "city": "São Paulo",
                "state": "SP",
                "zipcode": "01215010",
                "country": "Brasil",
                "id": 85267
            },
            "customer": {
                "object": "customer",
                "document_number": "85605046055",
                "document_type": "cpf",
                "name": "Teste",
                "email": "teste@hotmail.com",
                "born_at": null,
                "gender": "M",
                "date_created": "2017-01-17T18:48:39.848Z",
                "id": 140350
            },
            "card": {
                "object": "card",
                "id": "card_cixiw3v52007eqf6ep1drw7u4",
                "date_created": "2017-01-04T11:58:10.027Z",
                "date_updated": "2017-01-04T11:58:10.199Z",
                "brand": "visa",
                "holder_name": " TESTE",
                "first_digits": "424242",
                "last_digits": "4242",
                "country": "US",
                "fingerprint": "PEyFKWzMdB34",
                "valid": true,
                "expiration_date": "0120"
            },
            "split_rules": null,
            "antifraud_metadata": {},
            "metadata": {}
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
