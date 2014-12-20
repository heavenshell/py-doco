# -*- coding: utf-8 -*-
"""
    doco.tests.test_dialogue
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for dialogue.


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import simplejson as json
from unittest import TestCase
from mock import patch
from doco.client import Client


def dummy_response(m):
    import requests
    response = requests.Response()
    response.status_code = 200
    data = {
        'context': 'D0yHgwljc_mhTPIGs--toQ',
        'utt': 'ガッ', 'da': '0', 'yomi': 'ガッ', 'mode': 'dialog'
    }
    response._content = json.dumps(data)

    m.return_value = response


class TestDialogue(TestCase):
    def test_build_request(self):
        """ Dialogue().build_request() should update default user info. """
        user = {
            'nickname': 'foo',
            'bloodtype': 'O',
            'birthdateY': '1997',
            'birthdateM': '12',
            'birthdateD': '31'
        }
        c = Client(apikey='key', user=user)
        ret = c.apis['Dialogue'].build_request(age='17', mode='srtr',
                                               bloodtype='A')
        user['age'] = 17
        user['mode'] = 'srtr'
        user['bloodtype'] = 'A'
        self.assertEqual(sorted(ret), sorted(user))
        self.assertEqual(sorted(c.apis['Dialogue'].user), sorted(user))

    @patch('doco.requests.post')
    def test_parse_response(self, m):
        """ Dialogue().parse() should parse request to api. """
        dummy_response(m)
        c = Client(apikey='')
        c.send(utt=u'ぬるぽ', apiname='Dialogue')
        ret = c.apis['Dialogue'].parse(c.last_response)
        self.assertTrue(isinstance(ret, dict))

    @patch('doco.requests.post')
    def test_context(self, m):
        """ Dialogue().parse() should extract context. """
        dummy_response(m)
        c = Client(apikey='')
        c.send(utt=u'ぬるぽ', apiname='Dialogue')
        ret = c.apis['Dialogue'].parse(c.last_response)
        self.assertEqual(ret['context'], 'D0yHgwljc_mhTPIGs--toQ')
