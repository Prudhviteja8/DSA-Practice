# ============================================================
# CONTAINS DUPLICATE - Full Solution with Explanation
# ============================================================
# Problem: Given a list nums, return True if any value appears
#          more than once, and False if every element is unique.
#
# Example: [1, 2, 3, 1] -> True (1 appears twice)
#          [1, 2, 3, 4] -> False (all unique)
# ============================================================


# ----- THE SOLUTION -----

def containsDuplicate(nums):

    # Step 1: Create empty notebook (dictionary)
    # This stores numbers we have already seen
    notebook = {}

    # Step 2: Loop through each number
    for num in nums:

        # Step 3: Check if number is already in notebook
        # "Have I seen this number before?"
        if num in notebook:
            # YES -> duplicate found! Stop immediately.
            return True

        # Step 4: Number NOT in notebook, write it down
        # "Let me write this number so I remember I saw it"
        notebook[num] = True

    # Step 5: Finished entire loop, no duplicates found
    return False


# ----- TEST CASES -----

def test(nums):
    result = containsDuplicate(nums)
    print(f"nums = {nums}")
    print(f"Answer: {result}")
    print()


print("=" * 50)
print("TEST CASES")
print("=" * 50)
print()

# Test 1: [3, 7, 3, 5]
# num=3, notebook={}          -> NO, write {3:True}
# num=7, notebook={3:True}    -> NO, write {3:T, 7:T}
# num=3, notebook={3:T, 7:T}  -> YES! return True
test([3, 7, 3, 5])

# Test 2: [1, 2, 3, 4]
# All unique -> return False
test([1, 2, 3, 4])

# Test 3: [5, 5]
# num=5, notebook={}        -> NO, write {5:True}
# num=5, notebook={5:True}  -> YES! return True
test([5, 5])

# Test 4: [1, 2, 3, 1, 5]
# num=1 at step 4 already in notebook -> return True
test([1, 2, 3, 1, 5])

# Test 5: [10, 20, 30]
# All unique -> return False
test([10, 20, 30])
