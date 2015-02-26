# -*- coding: utf-8 -*-
"""
    doco
    ~~~~

    Docomo is a client library for docomo API.


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import requests

__version__ = '0.0.3'


class DocoError(Exception):
    """ Exception. """
    pass


class DocoInterface(object):
    #: Default log format.
    debug_log_format = (
        '[%(asctime)s %(levelname)s][%(pathname)s:%(lineno)d]: %(message)s'
    )

    """ Interface. """
    #: Default host.
    DEFAULT_HOST = 'api.apigw.smt.docomo.ne.jp'

    #: Url prefix required at header.
    url_prefix = 'https://{0}'.format(DEFAULT_HOST)

    #: Api key.
    apikey = None

    def _send(self, uri, params, headers):
        """Send request to API.

        :param uri: API uri
        :param params: Request params
        :param headers: Request header
        """
        response = requests.post(uri, data=params, headers=headers)
        if response.status_code == 200:
            return response

        raise DocoError('Status is {0}, params is {1} .'.format(
                        response.status_code, params))

    def send(self, **kwargs):
        """Send request to API.

        :param **kwargs:
        """
        raise NotImplementedError()

    def parse(self, response):
        """Parse response object.

        :param response:
        """
        raise NotImplementedError()
