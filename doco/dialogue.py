# -*- coding: utf-8 -*-
"""
    doco.dialogue
    ~~~~~~~~~~~~~

    docomo Dialogue api.

    https://dev.smt.docomo.ne.jp/?p=docs.api.page&api_docs_id=17#tag01


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import logging
import simplejson as json
from doco import DocoInterface

logger = logging.getLogger('doco')


class Dialogue(DocoInterface):
    #: Dialogue path.
    PATH = '/dialogue/v1/dialogue'

    #: Set dialogue charactor.
    charactor = {
        'kansai': 20,
        'baby': 30
    }

    def __init__(self, **kwargs):
        """Construct a Dialogue api request.

        :param **kwargs:
        """
        self.context = None
        self.user = {}

        args = [
            'nickname', 'nickname_y', 'sex', 'bloodtype',
            'birthdateY', 'birthdateM', 'birthdateD', 'age',
            'constellations', 'place', 'mode', 't'
        ]
        user = kwargs['user'] if 'user' in kwargs else None
        if user is not None and isinstance(user, dict):
            for arg in args:
                if arg in user:
                    self.user[arg] = user[arg]

    def build_request(self, **kwargs):
        """Build request body.

        :param **kwargs: Request args
        """
        body = {}
        if self.context is not None:
            body['context'] = self.context
            logger.info('context is `{0}`.'.format(body['context']))

        self.user.update(kwargs)
        user = self.user

        for k in user:
            if user[k] is not None:
                body[k] = user[k]

        return body

    def send(self, body=None, headers=None):
        """Send request.

        :param body: Request body
        :param headers: Request headers
        """
        uri = '{0}{1}?APIKEY={2}'.format(self.url_prefix, self.PATH,
                                         self.apikey)

        ret = self._send(uri, json.dumps(body), headers)

        return ret

    def parse(self, response):
        """Parse requests response.

        :param response: Parsed response dict
        """
        self.last_response = response
        response = json.loads(response.content)
        if 'context' in response:
            self.context = response['context']

        return response

    def refresh(self):
        """Refresh dialogue. """
        self.context = None
        self.response = None
