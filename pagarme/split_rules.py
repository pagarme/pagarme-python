# encoding: utf-8

from __future__ import unicode_literals

class SplitRules(object):

    def __init__(self, recipient_id=None, charge_processing_fee=None, liable=None,
                 percentage=None, amount=None, date_created=None, date_updated=None):

        self.data = {
            'recipient_id': recipient_id,
            'charge_processing_fee': charge_processing_fee,
            'liable': liable,
            'percentage': percentage,
            'amount': amount,
            'date_created': date_created,
            'date_updated': date_updated,
        }
        
    def get_split_data(self, cont):
        d = {}
        for key, value in self.data.items():
            if value:
                new_key = 'split_rules['+str(cont)+'][{key}]'.format(key=key)
                d[new_key] = value            
        return d