def ternarySearch(l, r, key, ar):
	while r >= l:
		mid1 = l + (r-l) // 3
		mid2 = r - (r-l) // 3
		
		if key == ar[mid1]:
			return mid1
		if key == ar[mid2]:
			return mid2
		if key < ar[mid1]:
			r = mid1 - 1
		elif key > ar[mid2]:
			l = mid2 + 1
		else:
			l = mid1 + 1
			r = mid2 - 1
	return -1

