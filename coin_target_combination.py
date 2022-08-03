def coin_subset_count(coins,target):
    dp=[0 for i in range(target+1)]
    dp[0]=1
    for i in range(len(coins)):
        for j in range(coins[i],len(dp)):
            dp[j]+=dp[j-coins[i]]
    return dp[target]



# ?can be done using 2d dp also , take target+1 cols , length coin+1 amount(0,1,..)
# for dp[0][0] keep it one
# if it is first row , fill with 0
# if it is first col . fill with 1
#  treat rest dp like seprate prob
# dp[i][j]=dp[i][j-coin[i]]+dp[i-1][j]
coins=[2,3,5,6]
target=10
print(coin_subset_count(coins,target))
