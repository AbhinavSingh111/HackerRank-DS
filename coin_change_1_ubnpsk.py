# coin change 1 problem
# it is a variation of count subset sum in unbounded knapsack
# we have to find the count of ways in which a given sum can be formed from the infinite supply of the given denomintation of coins

def coin_change_1(arr , s , n):
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if i==0:
                dp[i][j]=0
            if j==0:
                dp[i][j]=1
            elif arr[i-1]<=j:
                dp[i][j] = dp[i][j-arr[i-1]]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][s]

arr = [1,2,3,5]
s = 8
n = len(arr)
print(coin_change_1(arr , s , n))
