#n^3 complexity
#  def cost_of_painting(houses,n,c):
#     dp=[[0 for i in range(c)] for i in range(n)]
#     for i in range(c):
#         dp[0][i]=houses[0][i]

#     for i in range(1,n):
#         for j in range(c):
#             e = dp[i-1]
#             d = e[:]
#             d.pop(j)
#             dp[i][j] = houses[i][j]+min(d)
        
#     return min(dp[n-1])

# n^2 complxity
def cost_of_painting(houses,n,c):
    dp=[[0 for i in range(c)] for i in range(n)]
    least = 9999999
    sleast = 9999999
    for i in range(c):
        dp[0][i]=houses[0][i]
        if houses[0][i]<=least:
            sleast = least
            least = houses[0][i]
        elif houses[0][i]>=sleast:
            sleast=houses[0][i]

    for i in range(1,n):
        nleast=9999999
        nsleast=999999
        for j in range(c):
            if least==dp[i-1][j]:
                dp[i][j]=sleast+houses[i][j]
            else:
                dp[i][j]=least+houses[i][j]
            
            if dp[i][j]<=nleast:
                nsleast = nleast
                nleast = dp[i][j]
            elif dp[i][j]>=nsleast:
                nsleast=dp[i][j]
        least=nleast
        sleast=nsleast
        
    return least








n=4
c=6
houses=[[1,5,7,2,1,4],[5,8,4,3,6,1],[3,2,9,7,2,3],[1,2,4,9,1,7]]
print(cost_of_painting(houses,n,c))
