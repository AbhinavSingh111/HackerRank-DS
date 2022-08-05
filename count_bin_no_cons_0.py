# count of binary strings of length that do not have consecutive 0
# approach 1 using 2 arrays

def bin_count(n):
    dp0=[0 for i in range(n+1)]
    dp1=[0 for i in range(n+1)]
    dp0[1]=1
    dp1[1]=1
    for i in range(2,n+1):
        dp1[i]=dp1[i-1]+dp0[i-1]
        dp0[i]=dp1[i-1]
    return dp0[n]+dp1[n]

n=7
print(bin_count(n))
