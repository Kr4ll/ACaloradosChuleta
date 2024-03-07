def rec_binarysearch(e, elements):
    return __rec_bs__(e, 0, len(elements) - 1, elements)


def __rec_bs__(e, low, high, elements):
    # if not found
    # this element could be inserted at -index-1
    if low > high:
        return -low - 1
    mid = (low + high) // 2
    if elements[mid] == e:
        return mid  # found
    elif e < elements[mid]:
        return __rec_bs__(e, low, mid - 1, elements)
    else:
        return __rec_bs__(e, mid + 1, high, elements)
