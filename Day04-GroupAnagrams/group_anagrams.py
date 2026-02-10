# ============================================================
# GROUP ANAGRAMS - Full Solution with Explanation
# ============================================================
# Problem: Given a list of words, group the anagrams together.
#
# Example: ["eat","tea","tan","ate","nat","bat"]
#       -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]
#
# Trick: Sort each word's letters. Anagrams have the same
#        sorted form. Use sorted word as dictionary key.
# ============================================================


# ----- THE SOLUTION -----

def groupAnagrams(words):

    # Step 1: Create empty notebook
    notebook = {}

    # Step 2: Loop through each word
    for word in words:

        # Step 3: Sort the word -> use as key
        # "eat" -> "aet", "tea" -> "aet", "bat" -> "abt"
        key = "".join(sorted(word))

        # Step 4: Check if key exists in notebook
        if key in notebook:
            # YES -> add word to existing group
            notebook[key].append(word)
        else:
            # NO -> create new group with this word
            notebook[key] = [word]

    # Step 5: Return all groups
    return list(notebook.values())


# ----- TEST CASES -----

def test(words):
    result = groupAnagrams(words)
    print(f"words = {words}")
    print(f"Groups: {result}")
    print()


print("=" * 50)
print("TEST CASES")
print("=" * 50)
print()

# Test 1: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Walkthrough:
#   "eat" -> "aet" -> new group   {"aet": ["eat"]}
#   "tea" -> "aet" -> append      {"aet": ["eat","tea"]}
#   "tan" -> "ant" -> new group   {"aet": [...], "ant": ["tan"]}
#   "ate" -> "aet" -> append      {"aet": ["eat","tea","ate"], ...}
#   "nat" -> "ant" -> append      {..., "ant": ["tan","nat"]}
#   "bat" -> "abt" -> new group   {..., "abt": ["bat"]}
test(["eat", "tea", "tan", "ate", "nat", "bat"])

# Test 2: ["dog", "god", "cat", "act", "good"]
# "dog"/"god" -> "dgo", "cat"/"act" -> "act", "good" -> "dgoo"
test(["dog", "god", "cat", "act", "good"])

# Test 3: ["abc", "bca", "xyz", "zyx", "cab"]
# "abc"/"bca"/"cab" -> "abc", "xyz"/"zyx" -> "xyz"
test(["abc", "bca", "xyz", "zyx", "cab"])

# Test 4: ["hello"]
# Only one word -> one group
test(["hello"])

# Test 5: ["a", "b", "a"]
# "a"/"a" -> "a", "b" -> "b"
test(["a", "b", "a"])
