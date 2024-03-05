"""A basic hello world example of Hypothesis"""

from hypothesis import example, given, strategies as st
from hypothesis.strategies import text

def encode(input_string):
    count = 1
    prev = ""
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q

# This is the actual test
@given(st.text())
@example("")
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s

# This needs to exist at the bottom of each test scenario so it'll be run
if __name__ == "__main__":
    test_decode_inverts_encode()
