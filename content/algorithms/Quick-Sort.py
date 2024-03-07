def partition(arr, left, right):
	i = (left-1)
	pivot = arr[right]

	for j in range(left, right):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[right] = arr[right], arr[i+1]
	return (i+1)

def quicksort(arr):
	quicksort_rec(arr, 0, len(arr)-1)

def quicksort_rec(arr, left, right):
	if len(arr) == 1:
		return arr
	if left < right:
		pi = partition(arr, left, right)

		quicksort_rec(arr, left, pi-1)
		quicksort_rec(arr, pi+1, right)
