# coin change 2 problem
# it is a variation of count subset sum in unbounded knapsack
# here we need to initiallise 1st row with inf-1 and 1st col with 0
# then in 2nd row we need to divide the j with coin[0] if rem 0 then put ans , else inf-1
# for the rest use unknpsk with min in case of max
# we have to find the min number of coins necessary to get the sum

def coin_change_2(arr , s , n):
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if i==0:
                dp[i][j]=9999999-1
            else:
                dp[i][j]=0
    for j in range(1,s+1):
        if j%arr[0]==0:
            dp[1][j] = j//arr[0]
        else:
            dp[1][j] = 9999999-1

    for i in range(2,n+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                dp[i][j] = min(1+dp[i][j-arr[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][s]

arr = [1,2,3,5]
s = 5
n = len(arr)
print(coin_change_2(arr , s , n))
