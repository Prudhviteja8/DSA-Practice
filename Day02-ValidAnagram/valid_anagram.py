# ============================================================
# VALID ANAGRAM - Full Solution with Explanation
# ============================================================
# Problem: Given two strings s and t, return True if t is an
#          anagram of s, and False otherwise.
#
# Anagram: Same letters, same count, different order.
# Example: "rat" and "tar" -> True (both have r:1, a:1, t:1)
# ============================================================


# ----- THE SOLUTION -----

def isAnagram(s, t):

    # Step 1: Count letters in s
    # Create empty notebook, loop through each letter
    # If seen before -> add 1, if first time -> start at 1
    notebook1 = {}
    for letter in s:
        if letter in notebook1:
            notebook1[letter] = notebook1[letter] + 1
        else:
            notebook1[letter] = 1

    # Step 2: Count letters in t
    # Same counting logic for the second string
    notebook2 = {}
    for letter in t:
        if letter in notebook2:
            notebook2[letter] = notebook2[letter] + 1
        else:
            notebook2[letter] = 1

    # Step 3: Compare both notebooks
    # If same letters with same counts -> Anagram!
    return notebook1 == notebook2


# ----- TEST CASES -----

def test(s, t):
    result = isAnagram(s, t)
    print(f's = "{s}", t = "{t}"')
    print(f"Answer: {result}")
    print()


print("=" * 50)
print("TEST CASES")
print("=" * 50)
print()

# Test 1: "rat" and "tar"
# notebook1 = {r:1, a:1, t:1}
# notebook2 = {t:1, a:1, r:1}
# Same counts -> True
test("rat", "tar")

# Test 2: "cat" and "car"
# notebook1 = {c:1, a:1, t:1}
# notebook2 = {c:1, a:1, r:1}
# Different (t vs r) -> False
test("cat", "car")

# Test 3: "listen" and "silent"
# notebook1 = {l:1, i:1, s:1, t:1, e:1, n:1}
# notebook2 = {s:1, i:1, l:1, e:1, n:1, t:1}
# Same counts -> True
test("listen", "silent")

# Test 4: "aab" and "abb"
# notebook1 = {a:2, b:1}
# notebook2 = {a:1, b:2}
# Different counts -> False
test("aab", "abb")

# Test 5: "banana" and "ananab"
# notebook1 = {b:1, a:3, n:2}
# notebook2 = {a:3, n:2, b:1}
# Same counts -> True
test("banana", "ananab")
