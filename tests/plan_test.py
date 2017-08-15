from tests.resources.dictionaries import plan_dictionary
from pagarme import plan


def test_create_trial_plan():
    _plan = plan.create(plan_dictionary.TRIAL_PLAN)
    assert _plan['trial_days'] == 30


def test_create_no_trial_plan():
    _plan = plan.create(plan_dictionary.NO_TRIAL_PLAN)
    assert _plan['trial_days'] == 0


def test_create_boleto_plan():
    _plan = plan.create(plan_dictionary.BOLETO_PLAN)
    assert _plan['payment_methods'] == ["boleto"]


def test_create_credit_card_plan():
    _plan = plan.create(plan_dictionary.CREDIT_CARD_PLAN)
    assert _plan['payment_methods'] == ["credit_card"]


def test_find_all_plans():
    all_plans = plan.find_all()
    assert all_plans is not None


def test_find_by():
    _plan = plan.create(plan_dictionary.TRIAL_PLAN)
    find_plan = plan.find_by(_plan['id'])
    assert _plan['id'] == find_plan['id']


def test_update():
    _plan = plan.create(plan_dictionary.TRIAL_PLAN)
    assert _plan['trial_days'] == 30
    update_plan = plan.update(_plan['id'], plan_dictionary.UPDATE_PLAN)
    print(update_plan)
    assert update_plan['trial_days'] == 7