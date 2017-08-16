from tests.resources.dictionaries import subscription_dictionary
from pagarme import subscription


def test_create_boleto_subscription():
    _subscription = subscription.create(subscription_dictionary.BOLETO_SUBSCRIPTION)
    assert _subscription['payment_method'] == 'boleto'


def test_create_credit_card_subscription():
    _subscription = subscription.create(subscription_dictionary.CREDIT_CARD_SUBSCRIPTION)
    assert _subscription['payment_method'] == 'credit_card'


def test_find_all():
    subscription.create(subscription_dictionary.CREDIT_CARD_SUBSCRIPTION)
    all_subscriptions = subscription.find_all()
    assert all_subscriptions is not None


def test_find_by():
    _subscription = subscription.create(subscription_dictionary.CREDIT_CARD_SUBSCRIPTION)
    find_subscription = subscription.find_by(_subscription['id'])
    assert find_subscription['id'] == _subscription['id']


def test_update():
    _subscription = subscription.create(subscription_dictionary.CREDIT_CARD_SUBSCRIPTION)
    assert _subscription['payment_method'] == 'credit_card'
    updated_subscription = subscription.update(_subscription['id'], subscription_dictionary.UPDATE)
    assert updated_subscription['payment_method'] == 'boleto'


def test_cancel():
    _subscription = subscription.create(subscription_dictionary.BOLETO_SUBSCRIPTION)
    assert _subscription['status'] == 'unpaid'
    canceled_subscription = subscription.cancel(_subscription['id'])
    assert canceled_subscription['status'] == 'canceled'


def test_transactions():
    _subscription = subscription.create(subscription_dictionary.CREDIT_CARD_SUBSCRIPTION)
    subscription_transactions = subscription.transactions(_subscription['id'])
    assert subscription_transactions is not None


def test_settle_charges_params():
    _subscription = subscription.create(subscription_dictionary.BOLETO_SUBSCRIPTION)
    assert _subscription['status'] == 'unpaid'
    settle_charge_subscription = subscription.settle_charges(_subscription['id'], subscription_dictionary.CHARGES)
    assert settle_charge_subscription['status'] == 'paid'
    assert settle_charge_subscription['settled_charges'] == [1]

def test_settle_charges_no_params():
    _subscription = subscription.create(subscription_dictionary.BOLETO_SUBSCRIPTION)
    assert _subscription['status'] == 'unpaid'
    settle_charge_subscription = subscription.settle_charges(_subscription['id'])
    assert settle_charge_subscription['status'] == 'paid'
    assert settle_charge_subscription['settled_charges'] == [1]
