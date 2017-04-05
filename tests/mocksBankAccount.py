#encoding: utf-8
import json

class FakeResponse(object):
    status_code = 200
    content = '''
    {
        "object": "bank_account",
        "id": 17422412,
        "bank_code": "341",
        "agencia": "3209",
        "agencia_dv": "5",
        "conta": "58054",
        "conta_dv": "1",
        "type": "conta_corrente",
        "document_type": "cpf",
        "document_number": "26268738888",
        "legal_name": "BANK ACCOUNT PYTHON",
        "charge_transfer_fees": true,
        "date_created": "2017-03-08T18:29:09.644Z"
    }
    '''

    def json(self):
        return json.loads(self.content)

def fake_request_list(*args, **kwargs):
    fakeresponse = FakeResponse()
    fakeresponse.content = '[' + fakeresponse.content + ']'
    return fakeresponse

def fake_request(*args, **kwargs):
    return FakeResponse()

def fake_request_fail_api_key(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"api_key",
        "message":"api_key inv\xc3\xa1lida"}],
        "url":"/bank_accounts/17422412","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_id(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"id",
        "message":"bankAccount id inv\xc3\xa1lido"}],
        "url":"/bank_accounts/17422412","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_bank_code(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"bank_code",
        "message":"codigo do banco inv\xc3\xa1lido"}],
        "url":"/bank_accounts/0932","method":"get"
    }
    """
    fake.status_code = 400
    return fake


def fake_request_fail_agencia(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"agencia",
        "message":"numero de agencia inv\xc3\xa1lido"}],
        "url":"/bank_accounts/0932","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_agencia_dv(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"agencia_dv",
        "message":"digito verificador da agencia inv\xc3\xa1lido"}],
        "url":"/bank_accounts/5","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_conta(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"conta",
        "message":"numero de conta inv\xc3\xa1lida"}],
        "url":"/bank_accounts/58054","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_conta_dv(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"conta_dv",
        "message":"digito verificador de conta inv\xc3\xa1lido"}],
        "url":"/bank_accounts/1","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_type(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"type",
        "message":"tipo de conta inv\xc3\xa1lido verificar tipos na documentação"}],
        "url":"/bank_accounts/conta_qualquer","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_document_number(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"documet_number",
        "message":"numero de CPF ou CNPJ inv\xc3\xa1lido"}],
        "url":"/bank_accounts/26268738888","method":"get"
    }
    """
    fake.status_code = 400
    return fake

def fake_request_fail_legal_name(*args,**kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"bad request",
        "parameter_name":"legal_name",
        "message":"nome da conta bancaria inv\xc3\xa1lido"}],
        "url":"/bank_accounts/joao","method":"get"
    }
    """
    fake.status_code = 400
    return fake