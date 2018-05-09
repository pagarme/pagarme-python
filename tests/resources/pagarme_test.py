from datetime import datetime, timedelta
from pagarme.resources import handler_request
import time
import requests
import json

AUTH_TEST = handler_request.authentication_key(None, True)
POSTBACK_URL = 'http://teste.url.com'
BUSINESS_CALENDAR_URL = 'https://pagarme.github.io/business-calendar/data/brazil/{0}.json'


def create_postback_url():
    return POSTBACK_URL


def generate_timestamp():
    date = datetime.now() + timedelta(days=3)

    while is_holiday(date) or is_weekend(date):
        date = date + timedelta(days=2)

    return int(time.mktime(date.timetuple()) * 1000)


def is_holiday(date):
    year = date.year
    month = '0{0}'.format(date.month) if date.month < 10 else date.month
    day = '0{0}'.format(date.day) if date.day < 10 else date.day

    date = '{0}-{1}-{2}'.format(year, month, day)
    business_calendar = get_business_calendar(year)['calendar']
    for day in business_calendar:
        if date in day['date']:
            return True

    return False


def is_weekend(date):
    if date.strftime("%A") in ('Sunday', 'Saturday'):
        return True

    return False


def get_business_calendar(year):
    r = requests.get(BUSINESS_CALENDAR_URL.format(year))
    business_calendar = json.loads(r.content.decode('utf-8'))

    return business_calendar
