# Python 3 program to find lexicographically
# smallest sequence with rotations.
# Function to compare lexicographically
# two sequence with different starting
# indexes. It returns true if sequence
# beginning with y is lexicographically
# greater. O(n^2)
import copy
def printSmallestSequence(s):
    m = copy.copy(s)
    for i in range(len(s) - 1):
        if m > s[i:] + s[:i]:
            m = s[i:] + s[:i]
    return m
