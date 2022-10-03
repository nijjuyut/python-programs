#Sliding Window Algorithm in Python
#Time Comp: O(n * k)

import sys
INT_MIN = -sys.maxsize - 1

# Returns maximum sum in a
# subarray of size k.
def maxSum(arr, n, k):
	# Initialize result
	ma = INT_MIN

	for i in range(n - k + 1):
		curr = 0
    
		for j in range(k):
			curr = curr + arr[i + j]

		# Update result if condition satisfied
		ma = max(curr, ma)

	return ma



# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)

print(maxSum(arr, n, k))
