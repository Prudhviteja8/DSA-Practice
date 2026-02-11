# ============================================================
# TOP K FREQUENT ELEMENTS - Full Solution with Explanation
# ============================================================
# Problem: Given a list nums and a number k, return the k
#          most frequent (most repeated) numbers.
#
# Example: nums = [1,1,1,2,2,3], k = 2 -> [1, 2]
#          (1 appears 3 times, 2 appears 2 times -> top 2)
#
# Trick: Count each number, then sort by count, pick top k.
# ============================================================


# ----- THE SOLUTION -----

def topKFrequent(nums, k):

    # Step 1: Count each number
    notebook = {}
    for num in nums:
        if num in notebook:
            notebook[num] = notebook[num] + 1
        else:
            notebook[num] = 1

    # Step 2: Sort by count (highest first) and take top k
    result = sorted(notebook, key=lambda x: notebook[x], reverse=True)

    # Step 3: Return top k
    return result[:k]


# ----- TEST CASES -----

def test(nums, k):
    result = topKFrequent(nums, k)
    print(f"nums = {nums}, k = {k}")
    print(f"Answer: {result}")
    print()


print("=" * 50)
print("TEST CASES")
print("=" * 50)
print()

# Test 1: [1,1,1,2,2,3], k=2
# Count: {1:3, 2:2, 3:1} -> sorted: [1,2,3] -> top 2: [1,2]
test([1, 1, 1, 2, 2, 3], 2)

# Test 2: [5,5,3,3,3,1], k=1
# Count: {5:2, 3:3, 1:1} -> sorted: [3,5,1] -> top 1: [3]
test([5, 5, 3, 3, 3, 1], 1)

# Test 3: [7,7,2,2,2,1,1,1,1], k=2
# Count: {7:2, 2:3, 1:4} -> sorted: [1,2,7] -> top 2: [1,2]
test([7, 7, 2, 2, 2, 1, 1, 1, 1], 2)

# Test 4: [4,4,4,6,6,7,7,7,7], k=1
# Count: {4:3, 6:2, 7:4} -> sorted: [7,4,6] -> top 1: [7]
test([4, 4, 4, 6, 6, 7, 7, 7, 7], 1)
