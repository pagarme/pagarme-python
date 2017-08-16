from pagarme import balance


def test_default_recipeint_balance():
    _balance = balance.default_recipeint_balance()
    assert _balance['object'] == 'balance'
    assert _balance['available']['amount'] == 0
    assert _balance['waiting_funds']['amount'] == 9500
    assert _balance['transferred']['amount'] == 0