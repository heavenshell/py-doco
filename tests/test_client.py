# -*- coding: utf-8 -*-
"""
    domo.tests.test_client
    ~~~~~~~~~~~~~~~~~~~~~~

    Tests for docomo api.


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import simplejson as json
from mock import patch
from unittest import TestCase
from domo.client import Client


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


class TestClient(TestCase):
    def test_default_useragent(self):
        """ Default user-agent should be `Python client 0.0.1`."""
        c = Client(apikey='key')
        self.assertEqual(c.DEFAULT_USER_AGENT,
                         'Python client 0.0.1')

    def test_default_header(self):
        """ Default headers should contains user-agent. """
        c = Client(apikey='key')
        self.assertEqual(c.DEFAULT_HEADERS['User-Agent'], 'Python client 0.0.1')

    @patch('domo.requests.post')
    def test_send(self, m):
        """ Client().send() should send request to api. """
        dummy_response(m)
        c = Client(apikey='')
        ret = c.send(utt=u'ぬるぽ', apiname='Dialogue')
        self.assertEqual(ret['context'], 'D0yHgwljc_mhTPIGs--toQ')

    @patch('domo.requests.post')
    def test_last_response(self, m):
        """ Client().send() should send request to api and set response. """
        dummy_response(m)
        c = Client(apikey='')
        c.send(utt=u'ぬるぽ', apiname='Dialogue')
        self.assertEqual(c.last_response.status_code, 200)
