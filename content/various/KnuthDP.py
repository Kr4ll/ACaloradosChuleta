def minCost(arr, N):
    # Creating the prefix sum array
    pref = [0] * (N + 1)
    dp = [[0 for i in range(N)] for j in range(N)]
    opt = [[0 for i in range(N)] for j in range(N)]
 
    # Loop to calculate the prefix sum
    for i in range(N):
        pref[i + 1] = pref[i] + arr[i]
        opt[i][i] = i
    # Iterating through all sub-arrays
    # of length 2 or greater
    for i in range(N - 2, -1, -1):
        for j in range(i + 1, N):
            # Cost function = sum of
            # all elements in the sub-array
            cost = pref[j + 1] - pref[i]
            mn = float("inf")
            for k in range(opt[i][j - 1], min(j - 1, opt[i + 1][j]) + 1):
                if mn >= dp[i][k] + dp[k + 1][j] + cost:
                    # Updating opt table
                    opt[i][j] = k
                    # Updating minimum cost
                    mn = dp[i][k] + dp[k + 1][j] + cost
            # dp transition
            dp[i][j] = mn
    return dp[0][N - 1]
# Driver code
if __name__ == '__main__':
    arr = [3, 4, 2, 1, 7]
    N = len(arr)
    # Function call
    print(minCost(arr, N))
# Input: arr[] = {3, 4, 2, 1, 7}
# Output: 37
# Explanation: 
# Remove the elements at 0th and 1st index. arr[] = {7, 2, 1, 7}, Cost = 3 + 4 = 7
# Remove 1st and 2nd index elements. arr[] = {7, 3, 7}, Cost = 2 + 1 = 3
# Remove 1st and 2nd index elements, arr[] = {7, 10}, Cost = 3 + 7 = 10
# Remove the last two elements. arr[] = {17}, Cost =  = 7 + 10 = 17
# Total cost = 7 + 3 + 10 + 17 = 37
# This is the minimum possible total cost for this array.
