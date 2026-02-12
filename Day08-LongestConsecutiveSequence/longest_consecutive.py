# ============================================================
# LONGEST CONSECUTIVE SEQUENCE - Full Solution
# ============================================================
# Problem: Given a list of numbers, find the longest sequence
#          of consecutive numbers. Return the length.
#
# Example: [100, 4, 200, 1, 3, 2] -> 4 (sequence: 1,2,3,4)
#
# Trick: Use a SET. Find START numbers (num-1 not in set).
#        Count from each start using while loop.
# ============================================================


def longestConsecutive(nums):

    # Step 1: Create a set
    num_set = set(nums)

    # Step 2: Track the longest
    longest = 0

    # Step 3: Loop through each number
    for num in num_set:

        # Step 4: Is this the START?
        if num - 1 not in num_set:

            # Step 5: Count the sequence
            current = num
            count = 1

            while current + 1 in num_set:
                current = current + 1
                count = count + 1

            # Step 6: Update longest
            if count > longest:
                longest = count

    return longest


# ----- TEST CASES -----

def test(nums):
    result = longestConsecutive(nums)
    print(f"nums = {nums}")
    print(f"Longest consecutive sequence: {result}")
    print()


print("=" * 50)
print("TEST CASES")
print("=" * 50)
print()

test([100, 4, 200, 1, 3, 2])       # 4 (1,2,3,4)
test([3, 5, 1, 2, 8, 9, 10])       # 3 (1,2,3 or 8,9,10)
test([10, 5, 12, 11, 6, 7])        # 3 (5,6,7 or 10,11,12)
test([1, 9, 3, 2, 8, 4, 7])        # 4 (1,2,3,4)
test([0, 0])                        # 1
test([])                             # 0
