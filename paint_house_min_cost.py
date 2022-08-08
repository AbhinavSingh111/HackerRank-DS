#  There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. 

def cost_of_painting(houses,n):
    dp=[[0 for i in range(3)] for i in range(n)]
    dp[0][0]=houses[0][0]
    dp[0][1]=houses[0][1]
    dp[0][2]=houses[0][2]

    for i in range(1,n):
        dp[i][0] = houses[i][0]+min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = houses[i][1]+min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = houses[i][2]+min(dp[i-1][0],dp[i-1][1])
    return min(dp[n-1])








n=4
houses=[[1,5,7],[5,8,4],[3,2,9],[1,2,4]]
print(cost_of_painting(houses,n))
