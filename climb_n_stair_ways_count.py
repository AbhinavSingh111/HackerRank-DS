# this approach follows faith and expectation recursion
# this solves topdown
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

#  the above approach gives the paths , and also it is TLE when used for large numbers ,
# can be optimised using memoisation as multiple subproblems are being solved multiple times


#  this approach follows lvel adoption approach , goes from bottome to top,\
# base case gives answer
# print path


def climbStairs3(n,path):
    if n==0:
        print(path,end=" ")
        return
    elif n<0:
        return
    else:
        climbStairs3(n-1,'1'+path)
        climbStairs3(n-2,'2'+path)
        # climbStairs3(n-3,'3'+path)
n=4
print(climbStairs3(n,""))



# the next approach to count the number of paths is based on  the iterative approach
def climbStairs5(i):
    l=[0]*(i+1)
    l[0]=1
    for n in range(1,i+1):
        if n==1:
            l[n]=l[n-1]
        elif n==2:
            l[n]=l[n-1]+l[n-2]
        else:
            l[n]=l[n-1]+l[n-2]+l[n-3]
    return l[n]
n=10
print(climbStairs5(n))


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
