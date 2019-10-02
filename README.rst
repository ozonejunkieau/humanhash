aussiehash
==========

``aussiehash`` provides human-readable representations of digests.
Based on the ``humanhash`` codebase at https://github.com/blag/humanhash,
the dictionary has been updated to provide an Australian localisation. The
word list has been filtered to be SFW, use at your own discretion though!

Example
-------

.. code-block:: python

    >>> import humanhash

    >>> digest = '7528880a986c40e78c38115e640da2a1'
    >>> humanhash.humanize(digest)
    'sunnies-drink-woop-garbo'
    >>> humanhash.humanize(digest, words=6)
    'station-yabby-piker-pav-cockie-apples'

    >>> humanhash.uuid()
    ('furphy-back-daks-wombat', '8cdfd5e0ba2b48de89c8989f62a985b4')

Install
-------

This module is NOT YET available on PyPI as the ``aussiehash`` package. You can however
install it with ``pip``:

.. code-block:: bash

    $ pip install git+https://github.com/ozonejunkieau/humanhash.git

Caveats
-------

Don’t store the humanhash output, as its statistical uniqueness is only
around 1 in 4.3 billion. Its intended use is as a human-readable (and,
most importantly, **memorable**) representation of a longer digest,
unique enough for display in a user interface, where a user may need to
remember or verbally communicate the identity of a hash, without having
to remember a 40-character hexadecimal sequence. Nevertheless, you
should keep original digests around, then pass them through
``humanize()`` only as you’re displaying them.

How It Works
------------

The procedure for generating a humanhash involves compressing the input
to a fixed length (default: 4 bytes), then mapping each of these bytes
to a word in a pre-defined wordlist (a default wordlist is supplied with
the library). This algorithm is consistent, so the same input, given the
same wordlist, will always give the same output. You can also use your
own wordlist, and specify a different number of words for output.

Inspiration
-----------

- `Chroma-Hash`_ - A human-viewable representation of a hash (albeit not
  one that can be output on a terminal, or shouted down a hallway).
- `The NATO Phonetic Alphabet`_ - A great example of the trade-off
  between clarity of human communication and byte-wise efficiency of
  representation.

.. _Chroma-Hash: http://mattt.github.com/Chroma-Hash/
.. _The NATO Phonetic Alphabet: http://en.wikipedia.org/wiki/NATO_phonetic_alphabet
