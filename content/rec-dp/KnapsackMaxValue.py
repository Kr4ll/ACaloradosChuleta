# Knapsack problem to reach max value
def knapSack(W, wt, val, n): 
    # Making the dp array 
    dp = [0 for i in range(W+1)] 
    # Taking first i elements 
    for i in range(1, n+1): 
        # Starting from back, 
        # so that we also have data of 
        # previous computation when taking i-1 items 
        for w in range(W, 0, -1): 
            if wt[i-1] <= w: 
                # Finding the maximum value 
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1]) 
    # Returning the maximum value of knapsack 
    return dp[W] 
# Driver code 
if __name__ == '__main__': 
    profit = [60, 100, 120] 
    weight = [10, 20, 30] 
    W = 50
    n = len(profit) 
    print(knapSack(W, weight, profit, n)) 
