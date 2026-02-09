# ============================================================
# TWO SUM - Full Solution with Explanation
# ============================================================
# Problem: Given a list of numbers and a target, find TWO
#          indices whose values add up to the target.
#
# Example: nums = [5, 3, 6, 8], target = 11
#          Answer: [0, 2] because nums[0] + nums[2] = 5 + 6 = 11
# ============================================================


# ----- THE SOLUTION -----

def twosum(nums, target):

    # Step 1: Create empty notebook (dictionary)
    # This stores numbers we have already seen
    # Format: {number: index}
    notebook = {}

    # Step 2: Loop through each number with its index
    # enumerate gives us both: i = position, num = value
    # Example: [5, 3, 6, 8]
    #   Loop 1: i=0, num=5
    #   Loop 2: i=1, num=3
    #   Loop 3: i=2, num=6
    #   Loop 4: i=3, num=8
    for i, num in enumerate(nums):

        # Step 3: Calculate the complement
        # "I have num. What do I NEED to reach the target?"
        # complement = target - num
        # Example: target=11, num=5 → complement = 11-5 = 6
        complement = target - num

        # Step 4: Check if complement exists in notebook
        # "Did I see this number earlier?"
        if complement in notebook:

            # YES! Found it!
            # notebook[complement] = index where complement was seen
            # i = current index
            # Return BOTH indices as a list
            #
            # Example: complement=5, notebook={5: 0, 3: 1}
            #   notebook[5] = 0 (5 was seen at index 0)
            #   i = 2 (we are currently at index 2)
            #   Return [0, 2]
            return [notebook[complement], i]

        # Step 5: Complement NOT found, save current number
        # "Write my number and position in the notebook
        #  so future numbers can find me"
        # Example: num=5, i=0 → notebook becomes {5: 0}
        notebook[num] = i


# ----- TEST CASES -----

def test(nums, target):
    result = twosum(nums, target)
    i, j = result[0], result[1]
    print(f"nums = {nums}, target = {target}")
    print(f"Answer: {result}")
    print(f"Because nums[{i}] + nums[{j}] = {nums[i]} + {nums[j]} = {nums[i] + nums[j]}")
    print()


print("=" * 50)
print("TEST CASES")
print("=" * 50)
print()

# Test 1: nums = [5, 3, 6, 8], target = 11
# Walkthrough:
#   i=0, num=5, complement=6, notebook={}              → not found, write {5:0}
#   i=1, num=3, complement=8, notebook={5:0}            → not found, write {5:0, 3:1}
#   i=2, num=6, complement=5, notebook={5:0, 3:1}      → FOUND! 5 is at index 0
#   Return [0, 2] → nums[0]+nums[2] = 5+6 = 11
test([5, 3, 6, 8], 11)

# Test 2: nums = [4, 2, 7, 1], target = 9
# Walkthrough:
#   i=0, num=4, complement=5, notebook={}              → not found, write {4:0}
#   i=1, num=2, complement=7, notebook={4:0}            → not found, write {4:0, 2:1}
#   i=2, num=7, complement=2, notebook={4:0, 2:1}      → FOUND! 2 is at index 1
#   Return [1, 2] → nums[1]+nums[2] = 2+7 = 9
test([4, 2, 7, 1], 9)

# Test 3: nums = [1, 4, 9, 2], target = 6
# Walkthrough:
#   i=0, num=1, complement=5, notebook={}              → not found, write {1:0}
#   i=1, num=4, complement=2, notebook={1:0}            → not found, write {1:0, 4:1}
#   i=2, num=9, complement=-3, notebook={1:0, 4:1}     → not found, write {1:0, 4:1, 9:2}
#   i=3, num=2, complement=4, notebook={1:0, 4:1, 9:2} → FOUND! 4 is at index 1
#   Return [1, 3] → nums[1]+nums[3] = 4+2 = 6
test([1, 4, 9, 2], 6)

# Test 4: nums = [10, 20, 30], target = 40
# Walkthrough:
#   i=0, num=10, complement=30, notebook={}            → not found, write {10:0}
#   i=1, num=20, complement=20, notebook={10:0}         → not found, write {10:0, 20:1}
#   i=2, num=30, complement=10, notebook={10:0, 20:1}  → FOUND! 10 is at index 0
#   Return [0, 2] → nums[0]+nums[2] = 10+30 = 40
test([10, 20, 30], 40)
