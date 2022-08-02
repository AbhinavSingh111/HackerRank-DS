# you will always have to move to next column with each step , you can collect gold on the way
def MaxGoldDug(mine):
    m=len(mine) #rows
    n=len(mine[0]) #columns
    dp = [[0 for i in range(n)]for i in range(m)]
    for j in range(n-1,-1,-1):
        for i in range(m-1,-1,-1):
            if j==n-1:
                dp[i][j]=mine[i][j]
            elif i==0:
                dp[i][j]=mine[i][j] + max(dp[i][j+1],dp[i+1][j+1])
            elif i==m-1:
                dp[i][j]=mine[i][j] + max(dp[i][j+1],dp[i-1][j+1])
            else:
                dp[i][j] = mine[i][j] + max(dp[i][j+1],dp[i-1][j+1],dp[i+1][j+1])
    goldDigged = dp[0][0]
    for i in range(1,m):
        if dp[i][0]>goldDigged:
            goldDigged=dp[i][0]
    return goldDigged













# mine=[[0,1,4,2,8,2],[4,3,6,5,0,4],[1,2,4,1,4,6],[2,0,7,3,2,2],[3,1,5,9,2,4],[2,7,0,8,5,1]]
mine=[[0,6,0],[5,8,7],[0,9,0]]
print(MaxGoldDug(mine))
