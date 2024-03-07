def maxSum(arr, n, k):
	max_sum = -0x3f3f3f
	min_sum = 0x3f3f3f
	for i in range(n - k + 1):
		current_sum = 0
		for j in range(k):
			current_sum += arr[i + j]
		max_sum = max(current_sum, max_sum)
		min_sum = max(current_sum, min_sum)
	return max_sum
