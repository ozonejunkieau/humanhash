"""
aussiehash: Human-readable representations of digests, with an Australian twist.

The simplest ways to use this module are the :func:`humanize` and :func:`uuid`
functions. For tighter control over the output, see :class:`HumanHasher`.
"""

import operator
import uuid as uuidlib
import math
import sys

if sys.version_info.major == 3:  # pragma: nocover
    # Map returns an iterator in PY3K
    py3_map = map

    def map(*args, **kwargs):
        return [i for i in py3_map(*args, **kwargs)]

    # Functionality of xrange is in range now
    xrange = range


DEFAULT_WORDLIST = word_list = (
    "aerial",
    "ambo",
    "ankle",
    "apples",
    "arvo",
    "aussie",
    "avos",
    "back",
    "bail",
    "banana",
    "barbie",
    "barrack",
    "bathers",
    "battler",
    "beaut",
    "big",
    "bicky",
    "billabong",
    "billy",
    "bingle",
    "bities",
    "bitzer",
    "bloke",
    "bluey",
    "bodgy",
    "bondi",
    "bonzer",
    "boogie",
    "boomer",
    "bored",
    "bottle",
    "bounce",
    "bourke",
    "bowl",
    "brass",
    "brekkie",
    "brickie",
    "brizzie",
    "brumby",
    "budgie",
    "bunyip",
    "bushranger",
    "butcher",
    "cactus",
    "captain",
    "cark",
    "chokkie",
    "chook",
    "chrissie",
    "chuck",
    "chunder",
    "click",
    "clucky",
    "coathanger",
    "cobber",
    "cockie",
    "cockroach",
    "coldie",
    "come",
    "conch",
    "cooee",
    "cook",
    "corker",
    "cozzie",
    "cranky",
    "cream",
    "crook",
    "crow",
    "cubby",
    "dag",
    "daks",
    "damper",
    "date",
    "deadset",
    "dill",
    "dinkum",
    "dipstick",
    "dob",
    "docket",
    "doco",
    "dog",
    "doovalacky",
    "down",
    "drink",
    "drongo",
    "drum",
    "dunny",
    "earbashing",
    "ekka",
    "esky",
    "fair",
    "fairy",
    "flat",
    "flick",
    "fly",
    "footy",
    "freckle",
    "fremantle",
    "freo",
    "frog",
    "fruit",
    "full",
    "furphy",
    "gabba",
    "gafa",
    "galah",
    "garbo",
    "give",
    "gobful",
    "gobsmacked",
    "going",
    "goog",
    "greenie",
    "grinning",
    "grog",
    "grouse",
    "gutful",
    "handle",
    "harold",
    "heaps",
    "hoon",
    "hooroo",
    "hotel",
    "icy",
    "joey",
    "journo",
    "jug",
    "jumbuck",
    "kangaroos",
    "kelpie",
    "kindie",
    "larrikin",
    "lend",
    "lippy",
    "liquid",
    "lizard",
    "lollies",
    "london",
    "long",
    "lucky",
    "lunch",
    "milk",
    "lurk",
    "maccas",
    "mallee",
    "mate",
    "matilda",
    "mickey",
    "milko",
    "moolah",
    "mozzie",
    "muddy",
    "mug",
    "mull",
    "muster",
    "mystery",
    "nasho",
    "naughty",
    "never",
    "nipper",
    "offsider",
    "old",
    "oldies",
    "outback",
    "paddock",
    "pav",
    "piece",
    "piker",
    "pink",
    "plate",
    "polly",
    "porky",
    "port",
    "postie",
    "quid",
    "rage",
    "rapt",
    "ratbag",
    "raw",
    "rego",
    "rellie",
    "right",
    "ripper",
    "road",
    "roadie",
    "rock",
    "roo",
    "ropeable",
    "rort",
    "rotten",
    "rubbish",
    "salute",
    "salvos",
    "sandgroper",
    "sanger",
    "scratchy",
    "servo",
    "shark",
    "shonky",
    "shout",
    "show",
    "sickie",
    "skite",
    "sleepout",
    "smoko",
    "snag",
    "sook",
    "spag",
    "spit",
    "spruiker",
    "sprung",
    "squizz",
    "standover",
    "station",
    "stickybeak",
    "stoked",
    "strewth",
    "strides",
    "strine",
    "stubby",
    "stubby",
    "stuffed",
    "sunbake",
    "sunnies",
    "surfies",
    "swag",
    "swagman",
    "taswegian",
    "tea",
    "technicolor",
    "thingo",
    "thongs",
    "tickets",
    "togs",
    "too",
    "top",
    "trackies",
    "troppo",
    "trough",
    "truckie",
    "tucker",
    "ugg",
    "useful",
    "ute",
    "veggies",
    "waca",
    "weekend",
    "whinge",
    "whiteant",
    "wobbly",
    "wombat",
    "woop",
    "wowser",
    "wuss",
    "yabby",
    "yakka",
)


class HumanHasher(object):

    """
    Transforms hex digests to human-readable strings.

    The format of these strings will look something like:
    `victor-bacon-zulu-lima`. The output is obtained by compressing the input
    digest to a fixed number of bytes, then mapping those bytes to one of 256
    words. A default wordlist is provided, but you can override this if you
    prefer.

    As long as you use the same wordlist, the output will be consistent (i.e.
    the same digest will always render the same representation).
    """

    def __init__(self, wordlist=DEFAULT_WORDLIST):
        """
            >>> HumanHasher(wordlist=[])
            Traceback (most recent call last):
              ...
            ValueError: Wordlist must have exactly 256 items
        """
        if len(wordlist) != 256:
            raise ValueError("Wordlist must have exactly 256 items")
        self.wordlist = wordlist

    def humanize_list(self, hexdigest, words=4):
        """
        Human a given hexadecimal digest, returning a list of words.

        Change the number of words output by specifying `words`.

            >>> digest = '60ad8d0d871b6095808297'
            >>> HumanHasher().humanize_list(digest)
            ['cranky', 'mate', 'handle', 'bitzer']
        """
        # Gets a list of byte values between 0-255.
        bytes_ = map(
            lambda x: int(x, 16), map("".join, zip(hexdigest[::2], hexdigest[1::2]))
        )
        # Compress an arbitrary number of bytes to `words`.
        compressed = self.compress(bytes_, words)

        return [str(self.wordlist[byte]) for byte in compressed]

    def humanize(self, hexdigest, words=4, separator="-"):
        """
        Humanize a given hexadecimal digest.

        Change the number of words output by specifying `words`. Change the
        word separator with `separator`.

            >>> digest = '60ad8d0d871b6095808297'
            >>> HumanHasher().humanize(digest)
            'cranky-mate-handle-bitzer'
            >>> HumanHasher().humanize(digest, words=6)
            'snag-kangaroos-nasho-waca-ankle-muddy'
            >>> HumanHasher().humanize(digest, separator='*')
            'cranky*mate*handle*bitzer'
        """
        # Map the compressed byte values through the word list.
        return separator.join(self.humanize_list(hexdigest, words))

    @staticmethod
    def compress(bytes_, target):

        """
        Compress a list of byte values to a fixed target length.

            >>> bytes_ = [96, 173, 141, 13, 135, 27, 96, 149, 128, 130, 151]
            >>> list(HumanHasher.compress(bytes_, 4))
            [64, 145, 117, 21]

        If there are less than the target number bytes, return input bytes

            >>> list(HumanHasher.compress(bytes_, 15))  # doctest: +ELLIPSIS
            [96, 173, 141, 13, 135, 27, 96, 149, 128, 130, 151]
        """

        bytes_list = list(bytes_)

        length = len(bytes_list)
        # If there are less than the target number bytes, return input bytes
        if target >= length:
            return bytes_

        # Split `bytes` evenly into `target` segments
        # Each segment hashes `seg_size` bytes, rounded down for some
        seg_size = float(length) / float(target)
        # Initialize `target` number of segments
        segments = [0] * target
        seg_num = 0

        # Use a simple XOR checksum-like function for compression
        for i, byte in enumerate(bytes_list):
            # Divide the byte index by the segment size to assign its segment
            # Floor to create a valid segment index
            # Min to ensure the index is within `target`
            seg_num = min(int(math.floor(i / seg_size)), target - 1)
            # Apply XOR to the existing segment and the byte
            segments[seg_num] = operator.xor(segments[seg_num], byte)

        return segments

    def uuid(self, **params):

        """
        Generate a UUID with a human-readable representation.

        Returns `(human_repr, full_digest)`. Accepts the same keyword arguments
        as :meth:`humanize` (they'll be passed straight through).

            >>> import re
            >>> hh = HumanHasher()
            >>> result = hh.uuid()
            >>> type(result) == tuple
            True
            >>> bool(re.match(r'^(\w+-){3}\w+$', result[0]))
            True
            >>> bool(re.match(r'^[0-9a-f]{32}$', result[1]))
            True
        """
        digest = str(uuidlib.uuid4()).replace("-", "")
        return self.humanize(digest, **params), digest


DEFAULT_HASHER = HumanHasher()
uuid = DEFAULT_HASHER.uuid
humanize = DEFAULT_HASHER.humanize
humanize_list = DEFAULT_HASHER.humanize_list

if __name__ == "__main__":  # pragma: nocover
    import doctest

    # http://stackoverflow.com/a/25691978/6461688
    # This will force Python to exit with the number of failing tests as the
    # exit code, which should be interpreted as a failing test by Travis.
    sys.exit(doctest.testmod())
