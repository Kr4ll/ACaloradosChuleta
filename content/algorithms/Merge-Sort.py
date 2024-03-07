
def merge(left, right, v):
    k = l = r = 0
    while l < len(left) and r < len(right) and k < len(v):
        if left[l] <= right[r]:
            v[k] = left[l]
            l += 1
        else:
            v[k] = right[r]
            r += 1
        k += 1


    while l < len(left):
        v[k] = left[l]
        l += 1
    while r < len(right):
        v[k] = right[r]
        r += 1
        k +=1

def mergeSort(v):
    if len(v) == 1:
        return

    mid = len(v) // 2

    left = v[:mid]
    right = v[mid:]

    mergeSort(left)
    mergeSort(right)

    merge(left, right, v)
