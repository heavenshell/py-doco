# -*- coding: utf-8 -*-
"""
    doco.client
    ~~~~~~~~~~~

    Client for docomo API.


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
from doco import __version__, DocoInterface, DocoError
from doco.dialogue import Dialogue


class Client(object):
    #: User-Agent.
    DEFAULT_USER_AGENT = 'Python client {0}'.format(__version__)

    #: Headers.
    DEFAULT_HEADERS = {
        'User-Agent': DEFAULT_USER_AGENT,
        'Content-Type': 'application/json'
    }

    def __init__(self, apikey=None, **kwargs):
        """Construct client.

        :param apikey: Api key
        :param user: User specific infomation
        """
        self.apikey = apikey
        self.apis = {}
        self.last_response = None

        #: Default api call.
        self.register_api('Dialogue', Dialogue(**kwargs))

    def register_api(self, name, api):
        """Register api.

        :param name: Api name
        :param api: Api object
        """
        if isinstance(api, DocoInterface) is False:
            raise DocoError('Api should be implementation of DocoInterface.')

        self.apis[name] = api

    def send(self, apiname, **kwargs):
        """Send request to docomo api.

        :param apiname: Api name
        :param **kwargs: Request args
        """
        obj = self.apis[apiname]
        obj.apikey = self.apikey
        body = obj.build_request(**kwargs)

        headers = None
        if 'headers' in kwargs:
            headers = kwargs['headers']
            headers = self.DEFAULT_HEADERS.update(headers)
        else:
            headers = self.DEFAULT_HEADERS

        result = obj.send(body=body, headers=headers)
        self.last_response = result
        response = obj.parse(result)

        return response
