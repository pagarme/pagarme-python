from pagarme import subscription
from pagarme import transaction
from tests.resources.dictionaries import subscription_dictionary
from tests.resources.dictionaries import transaction_dictionary
import time


def test_cancel():
    _subscription = subscription.create(subscription_dictionary.BOLETO_SUBSCRIPTION)
    assert _subscription['status'] == 'unpaid'
    canceled_subscription = subscription.cancel(_subscription['id'])
    assert canceled_subscription['status'] == 'canceled'


def test_create_boleto_subscription():
    _subscription = subscription.create(subscription_dictionary.BOLETO_SUBSCRIPTION)
    assert _subscription['payment_method'] == 'boleto'


def test_create_credit_card_subscription():
    _subscription = subscription.create(subscription_dictionary.CREDIT_CARD_SUBSCRIPTION)
    assert _subscription['payment_method'] == 'credit_card'


def test_create_split_rule_percentage_subscription():
    _subscription = subscription.create(subscription_dictionary.CREDIT_CARD_PERCENTAGE_SPLIT_RULE_SUBSCRIPTION)
    time.sleep(3)
    search_params = {'id': str(_subscription['current_transaction']['id'])}
    _transaction = transaction.find_by(search_params)
    assert _transaction[0]['split_rules'] is not None


def test_find_all():
    subscription.create(subscription_dictionary.CREDIT_CARD_SUBSCRIPTION)
    all_subscriptions = subscription.find_all()
    assert all_subscriptions is not None


def test_find_by():
    _subscription = subscription.create(subscription_dictionary.CREDIT_CARD_SUBSCRIPTION)
    time.sleep(3)
    search_params = {'id': str(_subscription['id'])}
    find_subscription = subscription.find_by(search_params)
    assert find_subscription[0]['id'] == _subscription['id']


def test_postbacks_find_all():
    _subscription = subscription.create(subscription_dictionary.BOLETO_SUBSCRIPTION)
    transaction.pay_boleto(_subscription['current_transaction']['id'], transaction_dictionary.PAY_BOLETO)
    time.sleep(3)
    _postbacks = subscription.postbacks(_subscription['id'])
    assert _postbacks[0]['model_id'] == str(_subscription['id'])


def test_postbacks_redeliver():
    _subscription = subscription.create(subscription_dictionary.BOLETO_SUBSCRIPTION)
    time.sleep(3)
    _transaction = subscription.transactions(_subscription['id'])
    assert _transaction[0]['status'] == 'waiting_payment'
    transaction.pay_boleto(_transaction[0]['id'], transaction_dictionary.PAY_BOLETO)
    time.sleep(3)
    search_params = {'id': _transaction[0]['id']}
    _transaction_paid = transaction.find_by(search_params)
    assert _transaction_paid[0]['status'] == 'paid'
    _postbacks = subscription.postbacks(_subscription['id'])
    redeliver = subscription.postback_redeliver(_subscription['id'], _postbacks[0]['id'])
    assert redeliver['status'] == 'pending_retry'


def test_settle_charges_no_params():
    _subscription = subscription.create(subscription_dictionary.BOLETO_SUBSCRIPTION)
    assert _subscription['status'] == 'unpaid'
    settle_charge_subscription = subscription.settle_charges(_subscription['id'])
    assert settle_charge_subscription['status'] == 'paid'
    assert settle_charge_subscription['settled_charges'] == [1]


def test_settle_charges_params():
    _subscription = subscription.create(subscription_dictionary.BOLETO_SUBSCRIPTION)
    assert _subscription['status'] == 'unpaid'
    settle_charge_subscription = subscription.settle_charges(_subscription['id'], subscription_dictionary.CHARGES)
    assert settle_charge_subscription['status'] == 'paid'
    assert settle_charge_subscription['settled_charges'] == [1]


def test_transactions():
    _subscription = subscription.create(subscription_dictionary.CREDIT_CARD_SUBSCRIPTION)
    subscription_transactions = subscription.transactions(_subscription['id'])
    assert subscription_transactions is not None


def test_update():
    _subscription = subscription.create(subscription_dictionary.CREDIT_CARD_SUBSCRIPTION)
    assert _subscription['payment_method'] == 'credit_card'
    updated_subscription = subscription.update(_subscription['id'], subscription_dictionary.UPDATE)
    assert updated_subscription['payment_method'] == 'boleto'
