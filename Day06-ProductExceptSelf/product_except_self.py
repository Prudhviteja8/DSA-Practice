# ============================================================
# PRODUCT OF ARRAY EXCEPT SELF - Full Solution with Explanation
# ============================================================
# Problem: Given a list nums, return a new list where each
#          position has the product of all numbers EXCEPT itself.
#
# Example: nums = [1,2,3,4] -> [24, 12, 8, 6]
#          answer[0] = 2*3*4 = 24 (everything except 1)
#          answer[1] = 1*3*4 = 12 (everything except 2)
#
# Trick: For each position = LEFT products x RIGHT products
# ============================================================


# ----- THE SOLUTION -----

def productExceptSelf(nums):

    n = len(nums)

    # Step 1: Build left products (left to right)
    # left[i] = product of all numbers to the LEFT of i
    left = []
    product = 1
    for i in range(n):
        left.append(product)          # save product BEFORE multiplying
        product = product * nums[i]   # multiply for next position

    # Step 2: Build right products (right to left)
    # right[i] = product of all numbers to the RIGHT of i
    right = [0] * n
    product = 1
    for i in range(n - 1, -1, -1):
        right[i] = product             # save product BEFORE multiplying
        product = product * nums[i]    # multiply for next position

    # Step 3: Multiply left x right
    answer = []
    for i in range(n):
        answer.append(left[i] * right[i])

    return answer


# ----- TEST CASES -----

def test(nums):
    result = productExceptSelf(nums)
    print(f"nums = {nums}")
    print(f"Answer: {result}")
    print()


print("=" * 50)
print("TEST CASES")
print("=" * 50)
print()

# Test 1: [1, 2, 3, 4]
# left  = [1, 1, 2, 6]
# right = [24, 12, 4, 1]
# answer = [24, 12, 8, 6]
test([1, 2, 3, 4])

# Test 2: [2, 3, 4]
# left  = [1, 2, 6]
# right = [12, 4, 1]
# answer = [12, 8, 6]
test([2, 3, 4])

# Test 3: [1, 2, 3, 4, 5]
# answer = [120, 60, 40, 30, 24]
test([1, 2, 3, 4, 5])

# Test 4: [-1, 1, 0, -3]
# answer = [0, 0, 3, 0]
test([-1, 1, 0, -3])
