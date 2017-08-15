from tests.resources.dictionaries import card_dictionary
from pagarme import card

def test_create_card():
    _card = card.create(card_dictionary.VALID_CARD_DICTIONARY)
    assert _card['id'] is not None

def test_find_all():
    cards = card.find_all()
    assert cards is not None

def test_find_by():
    _card = card.create(card_dictionary.VALID_CARD_DICTIONARY)
    find_card = card.find_by(_card['id'])
    assert _card['id'] == find_card['id']
