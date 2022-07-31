def climb_stairs_with_minimum_moves(moves):
    n = len(moves)
    dp = [None]*(n+1)
    dp[n]=0
    for i in range(n-1,-1,-1):
        if moves[i]>0:
            mini = 100000009
            for j in range(1,moves[i]+1):
                if i+j<len(dp):
                    if dp[i+j]!=None:
                        mini = min(mini,dp[i+j])
            if mini!=100000009:
                dp[i]=mini+1
    return dp[0]








moves=[3,2,0,4,2,0,2,3,1,2,2]
print(climb_stairs_with_minimum_moves(moves))
