# subset sum problem 
# it is a variation of 01 knapsack
def subset_sum(arr , sum ,n):
    dp = [[False for i in range(sum+1) ]for j in range(n+1)]
    for i in range (n+1):
        for j in range(sum+1):
            if i==0 :
                dp[i][j]=False
            if  j==0 :
                dp[i][j]=True

            elif arr[i-1]<=j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]

arr=[2 , 3, 7 , 8, 10]
sum= 67
n=len(arr)
print(subset_sum(arr , sum ,n))
