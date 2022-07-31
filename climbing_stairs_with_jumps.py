def climbStairsVariableJumps(i):
    n=len(i)
    l=[0]*(n+1)
    l[n]=1
    for j in range(n-1,-1,-1):
        for k in range(1,i[j]+1):
            if j+k<len(l):
                l[j]+=l[j+k]
    return l[0]

n=[3,3,0,2,2,3]
# n=[5,5,2,4,1,5,9,8,6,3,8,9,1]
print(climbStairsVariableJumps(n))
