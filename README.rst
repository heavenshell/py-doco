Domo
====
Client library for docomo API written in Python. 

https://dev.smt.docomo.ne.jp/?p=docs.index

Supported apis
--------------
- Dialogue

Sample code
-----------

..
  >>> from domo.client import Client                                              >>> c = Client(apikey='YOUR_API_KEY')
  >>> res = c.send(utt='hello', apiname='Dialogue')
  >>> print(res.status_code)
  200
  >>> print(res.headers)
  {'Content-Length': '99', 'Connection': 'keep-alive', 'Content-Type': 'application/json;charset=UTF-8', 'Date': 'Wed, 17 Dec 2014 05:28:28 GMT', 'asyncServiceInvoke': 'false'}
  >>> print(res.content.decode('utf-8'))
  {"utt":"はろー","yomi":"はろー","mode":"dialog","da":"30","context":"7DGIKMpQDE0zrQrYFAMqdw"}


Cli example
-----------

..
  $ cd examples
  $ python examples/dialogue_cli.py -u こんにちは
  'mode': 'dialog', 'utt': 'どうも', 'context': 'N1liohyhkp6K7M80KS3bwg', 'da': '0', 'yomi': 'どうも'}
  $ python dialogue_cli.py -i

Interactive shell mode
~~~~~~~~~~~~~~~~~~~~~~

..
  $ python examples/dialogue_cli.py -i
  Welcome to docomo dialogue cli.
  ^D to exit.
  >>> こんにちは
  はろー
  >>>

Shiritori mode
~~~~~~~~~~~~~~

..
  $ python examples/dialogue_cli.py -i -s
  Welcome to docomo dialogue cli.
  ^D to exit.
  >>> しりとり
  リング
  >>> グッズ
  頭痛
  >>> 海
  道のり
  >>> リンゴ
  ゴリラ
  >>> ラッパ
  パスポート
  >>>
