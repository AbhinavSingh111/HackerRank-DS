# how the n number of friends can be grouped , single or paired.

def pairing(friends):
    dp = [0 for i in range(friends+1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3,friends+1):
        dp[i] = dp[i-1] + (i-1)*dp[i-2]
    return dp[friends]








friends = 5
print(pairing(friends))
