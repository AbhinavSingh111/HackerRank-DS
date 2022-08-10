# n represents the length of floor 2 m wide
# you are given infinite supply of 2*1 m wide tiles
#  calculate number of ways in which the floor can be tiled

# use s to d diagram
# from source you need to calculate f(m-1) [if tiles put vertically]
# and f(m-2) [if tiles put horizontally]
# return f(m-1)+f(m-2)
# kind of fibonbacci logic

def floor_tiles(n):
    dp = [0 for i in range(n+1)]
    dp[1] = 1 # if the lenght of floor is 1 , we have only one way
    dp [2] = 2 # if the lenght of floor is 2 , we have only two way ,h&v
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]



# or use direct fibbonacci logic
def floor_tiles(N):
    MOD = 1000000007
    if N==1:
        return 1
    if N==2:
        return 2
    dp1 = 1
    dp2 = 2
    for i in range(3,N+1):
        dp = (dp1+dp2)%MOD
        dp1=dp2
        dp2=dp
    return dp%MOD


n = 4
print(floor_tiles(n))
