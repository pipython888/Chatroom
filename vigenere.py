import string

KEY = "3zMtuO_cdLJgg2v'>jQB SG5hb64Nw*bHPf'0Fo0q{"
CHARS = string.printable


def index(li, idx):
    return li[idx % len(li)]


def encode(text):
    result = []
    for x, y in zip(text, KEY):
        result.append(index(
            CHARS,
            CHARS.index(x) + CHARS.index(y)
        ))
    return ''.join(result)


def decode(text):
    result = []
    for x, y in zip(text, KEY):
        result.append(index(
            CHARS,
            CHARS.index(x) - CHARS.index(y)
        ))
    return ''.join(result)
