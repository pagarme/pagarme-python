from pagarme import postback
import pytest

PAYLOAD = 'id=2727403&fingerprint=bbf609f80b08e14b706cfdcb0d07948d5fafe42e&event=transaction_status_changed&old_status=processing&desired_status=waiting_payment&current_status=waiting_payment&object=transaction&transaction%5Bobject%5D=transaction&transaction%5Bstatus%5D=waiting_payment&transaction%5Brefuse_reason%5D=&transaction%5Bstatus_reason%5D=acquirer&transaction%5Bacquirer_response_code%5D=&transaction%5Bacquirer_name%5D=pagarme&transaction%5Bacquirer_id%5D=5a54a9e61aac296c19e4c838&transaction%5Bauthorization_code%5D=&transaction%5Bsoft_descriptor%5D=&transaction%5Btid%5D=2727403&transaction%5Bnsu%5D=2727403&transaction%5Bdate_created%5D=2018-01-09T11%3A41%3A26.624Z&transaction%5Bdate_updated%5D=2018-01-09T11%3A41%3A27.216Z&transaction%5Bamount%5D=1000&transaction%5Bauthorized_amount%5D=1000&transaction%5Bpaid_amount%5D=0&transaction%5Brefunded_amount%5D=0&transaction%5Binstallments%5D=1&transaction%5Bid%5D=2727403&transaction%5Bcost%5D=0&transaction%5Bcard_holder_name%5D=&transaction%5Bcard_last_digits%5D=&transaction%5Bcard_first_digits%5D=&transaction%5Bcard_brand%5D=&transaction%5Bcard_pin_mode%5D=&transaction%5Bpostback_url%5D=https%3A%2F%2Frequestb.in%2F1234&transaction%5Bpayment_method%5D=boleto&transaction%5Bcapture_method%5D=ecommerce&transaction%5Bantifraud_score%5D=&transaction%5Bboleto_url%5D=https%3A%2F%2Fpagar.me&transaction%5Bboleto_barcode%5D=1234%205678&transaction%5Bboleto_expiration_date%5D=2018-01-16T02%3A00%3A00.000Z&transaction%5Breferer%5D=api_key&transaction%5Bip%5D=179.191.121.66&transaction%5Bsubscription_id%5D=&transaction%5Bphone%5D=&transaction%5Baddress%5D=&transaction%5Bcustomer%5D%5Bobject%5D=customer&transaction%5Bcustomer%5D%5Bid%5D=442866&transaction%5Bcustomer%5D%5Bexternal_id%5D=&transaction%5Bcustomer%5D%5Btype%5D=&transaction%5Bcustomer%5D%5Bcountry%5D=&transaction%5Bcustomer%5D%5Bdocument_number%5D=11111111111&transaction%5Bcustomer%5D%5Bdocument_type%5D=cpf&transaction%5Bcustomer%5D%5Bname%5D=Leonardim%20de%20Deos&transaction%5Bcustomer%5D%5Bemail%5D=&transaction%5Bcustomer%5D%5Bphone_numbers%5D=&transaction%5Bcustomer%5D%5Bborn_at%5D=&transaction%5Bcustomer%5D%5Bbirthday%5D=&transaction%5Bcustomer%5D%5Bgender%5D=&transaction%5Bcustomer%5D%5Bdate_created%5D=2018-01-09T11%3A41%3A26.583Z&transaction%5Bbilling%5D=&transaction%5Bshipping%5D=&transaction%5Bcard%5D=&transaction%5Bsplit_rules%5D=&transaction%5Breference_key%5D=&transaction%5Bdevice%5D=&transaction%5Blocal_transaction_id%5D=&transaction%5Blocal_time%5D=&transaction%5Bfraud_covered%5D=false'
SIGNATURE = 'sha1=1b66c265fdac6a903d2aecd01290a26a17c246fd'
API_KEY = 'ak_test_21eI4THNDJx7vkJRuAmXYlFACIaxnS'


def test_failure_with_no_api_key():
    with pytest.raises(Exception) as info:
        postback.validate(SIGNATURE, PAYLOAD, '')

    message = str(info.value)

    assert message == 'Missing api_key.'


def test_success_validation_postback():
    _validation = postback.validate(SIGNATURE, PAYLOAD, API_KEY)

    assert _validation is True


def test_failure_validation_postback():
    _validation = postback.validate(SIGNATURE, '')

    assert _validation is False
