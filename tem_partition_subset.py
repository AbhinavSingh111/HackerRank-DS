# partition n members into k teams such that no teams are empty
def partition(members,teams):
    if members<teams or members==0 or teams == 0:
        return 0
    dp = [[0 for i in range(members+1)]for i in range(teams+1)]
    for i in range(1 , teams+1 ):
        for j in range(1,members+1):
            if  j<i:
                dp[i][j]=0
            elif j==i:
                dp[i][j]=1
            else:
                dp[i][j] = dp[i][j-1]*i+dp[i-1][j-1]
    return dp[teams][members]


    






members = 4
teams = 3
print(partition(members,teams))
