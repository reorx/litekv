LiteKV - Redis like wrapper for sqlite3
=======================================

LiteKV is a wrapper for sqlite3, it turns sqlite3 into a kv data store,
and has similar APIs with redis-py.

Simply execute ``python -m litekv`` (if you have installed it) or ``python litekv.py`` to run doctest.


Usage
-----

.. code:: python

    >>> db = LiteKV(reset=True)
    >>> db.set('a', '1')
    >>> db.get('a')
    '1'
    >>> db.set('a', '2')
    >>> db.get('a')
    '2'
    >>> db.set('b', '3')
    >>> list(db.keys())
    ['a', 'b']
    >>> db.delete('a')
    >>> db.get('a') is None
    True


Benchmark
---------

::

    $ python -m litekv --benchmark
    With rowid
    Do 10000 inserts & reads
    1215.88587897 Insertion per second
    18041.2587533 Reads per second

    Without rowid
    Do 10000 inserts & reads
    1182.05950852 Insertion per second
    17828.1725067 Reads per second
