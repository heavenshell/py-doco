#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    doco.examples.dialogue_cli
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Example of clie application.


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
import sys
import code
import argparse
import logging
sys.path.append(os.path.abspath(os.path.pardir))

from doco import DocoInterface
from doco.client import Client


def write(msg):
    msg = '\033[37m{0}\033[0m'.format(msg)
    sys.stdout.write(msg)
    sys.stdout.write('\n')


class Console(code.InteractiveConsole):
    def __init__(self, local=None, filename='<console>'):
        code.InteractiveConsole.__init__(self, local, filename)
        self.client = None

    def push(self, line):
        res = self.client.send(utt=line, apiname='Dialogue')
        write(res['utt'])


def parse_option():
    """Parse options.

    ================= =========== ==============
    Options           Default     Description
    ================= =========== ==============
    -m, --mode        Dialogue    Chat to bot
    -k, --apikey      None        Api key
    -u, --utt         None        Utt
    -s, --shiritori   shiritori   Shiritori mode
    -t, --type        None        Character type
    ================= =========== ==============

    """
    description = 'NTT docomo api library.'
    parser = argparse.ArgumentParser(description=description, add_help=False)
    parser.add_argument('-m', '--mode', default='Dialogue')
    parser.add_argument('-k', '--apikey', default=None)
    parser.add_argument('-u', '--utt', default=None)
    parser.add_argument('-i', '--intaractive', const=True, default=False,
                        nargs='?')
    parser.add_argument('-s', '--shiritori', const=True, default=False,
                        nargs='?')
    parser.add_argument('-t', '--type', default=None)
    parser.add_argument('-vv', '--verbose', default=False,
                        const=True, nargs='?')

    args = parser.parse_args()

    return args


def main():
    args = parse_option()
    apikey = args.apikey
    if apikey is None:
        apikey = os.environ['DOCO_API_KEY']

    if apikey is None:
        sys.exit(1)

    level = logging.INFO if args.verbose is True else logging.ERROR
    logging.basicConfig(level=level, format=DocoInterface.debug_log_format)

    shiritori = args.shiritori
    options = {}
    if shiritori is True:
        options['mode'] = 'srtr'
    if args.type is not None:
        options['t'] = args.type

    client = Client(apikey=apikey, user=options)
    if args.intaractive is False:
        if args.utt is None:
            sys.exit(1)
        res = client.send(utt=args.utt, apiname='Dialogue')
        write(str(res))
    else:
        console = Console()
        console.client = client
        sys.ps1 = '>>> '
        console.interact('Welcome to docomo dialogue cli.\n^D to exit.')


if __name__ == '__main__':
    main()
