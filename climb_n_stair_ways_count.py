def climbStairs(n):
    if n==0:
        return [""]
    elif n<0:
        return []
    else:
        p1=climbStairs(n-1)
        p2=climbStairs(n-2)
        paths=[]
    for i in p1:
        paths.append('1'+i)
    for i in p2:
        paths.append('2'+i)
    return paths
n=35
print(climbStairs(n))

#  the above approach gives the paths , and also it is TLE

# the next step to count the number of paths is based on fibonacci approach
def climbStairs(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a,b,c=1,1,0
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
    return c
n=35
print(climbStairs(n))
