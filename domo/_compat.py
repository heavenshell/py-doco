# -*- coding: utf-8 -*-
"""
    Add comment here
    ~~~~~~~~~~~~~~~~

    Copied from `werkzuig._compat.py`.
    see https://github.com/mitsuhiko/werkzeug/blob/master/werkzeug/_compat.py

    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import sys

PY2 = sys.version_info[0] == 2

if PY2:
    text_type = unicode

    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()

    def to_bytes(x, charset=sys.getdefaultencoding(), errors='strict'):
        if x is None:
            return None
        if isinstance(x, (bytes, bytearray, buffer)):
            return bytes(x)
        if isinstance(x, unicode):
            return x.encode(charset, errors)
        raise TypeError('Expected bytes')
else:
    text_type = str

    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())

    def to_bytes(x, charset=sys.getdefaultencoding(), errors='strict'):
        if x is None:
            return None
        if isinstance(x, (bytes, bytearray, memoryview)):
            return bytes(x)
        if isinstance(x, str):
            return x.encode(charset, errors)
        raise TypeError('Expected bytes')


def to_unicode(x, charset=sys.getdefaultencoding(), errors='strict',
               allow_none_charset=False):
    """Copied from `werkzuig._compat.py`.

    see https://github.com/mitsuhiko/werkzeug/blob/master/werkzeug/_compat.py
    """
    if x is None:
        return None
    if not isinstance(x, bytes):
        return text_type(x)
    if charset is None and allow_none_charset:
        return x
    return x.decode(charset, errors)
