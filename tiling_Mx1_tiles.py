# n*m represents the dimensions of floor
# you are given infinite supply of M*1 m wide tiles
#  calculate number of ways in which the floor can be tiled

# use s to d diagram
# from source you need to calculate f(n,m-1) [if tiles put vertically]
# and f(n,m-n) [if tiles put horizontally]
# return f(n,m-1)+f(n,m-n)
# kind of fibonbacci logic but not similar

def floor_tiles(n,m):
    dp = [0 for i in range(n+1)]
    for i in range(1, n+1):
        if i < m :
            dp[i]=1
        elif i==m:
            dp[i]=2
        else:
            dp[i] = dp[i-1]+dp[i-m] 

        
    return dp[n]




n = 8
m = 3
print(floor_tiles(n,m))
