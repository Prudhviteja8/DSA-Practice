# ============================================================
# ENCODE AND DECODE STRINGS - Full Solution
# ============================================================
# Problem: Design encode and decode functions.
# Encode: list of strings -> single string
# Decode: single string -> list of strings
#
# Trick: Before each word, write length + "#"
# "hello" -> "5#hello"
# ============================================================


def encode(strs):
    result = ""
    for word in strs:
        result = result + str(len(word)) + "#" + word
    return result


def decode(s):
    result = []
    i = 0
    while i < len(s):
        j = s.find("#", i)
        length = int(s[i:j])
        word = s[j + 1 : j + 1 + length]
        result.append(word)
        i = j + 1 + length
    return result


# ----- TEST CASES -----

def test(words):
    encoded = encode(words)
    decoded = decode(encoded)
    print(f"Original: {words}")
    print(f"Encoded:  {encoded}")
    print(f"Decoded:  {decoded}")
    print(f"Match:    {words == decoded}")
    print()


print("=" * 50)
print("TEST CASES")
print("=" * 50)
print()

test(["hello", "world"])
test(["hi", "bye", "ok"])
test(["he,llo", "wo,rld"])
test(["", "hello", ""])
test(["a"])
