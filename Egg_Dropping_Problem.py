# Egg Dropping Problem Recursive
# variation of MCM
# given a floor number , number of eggs , find out the critical floor /  threshold floor form where the egg if thrown will not break , using minimum attempts 
# Problem statement: You are given N floor and K eggs. You have to minimize the number of times you have to drop the eggs to find the critical floor where critical floor means the floor beyond which eggs start to break. Assumptions of the problem:

# If egg breaks at ith floor then it also breaks at all greater floors.
# If egg does not break at ith floor then it does not break at all lower floors.
# Unbroken egg can be used again.
# Note: You have to find minimum trials required to find the critical floor not the critical floor.

# Example:
# Input:
#     4
#     2
    
#     Output:
#     Number of trials when number of eggs is 2 and number of floors is 4: 3
#

# recursive version

def egg_dropping_recursive(e  , f):
    if e==1:
        return f
    if f==1 or f ==0:
        return f
    ans = 9999999
    for k in range(1, f):
        temp = 1 + max(egg_dropping_recursive(e-1 , k-1) , egg_dropping_recursive(e , f-k))
        ans = min(ans , temp)
    return ans


f = 4
e = 2
print(egg_dropping_recursive(e , f))


# memoized version
dp = [[-1 for i in range(51)] for j in range(51)] #e is number of rows and j is number of columns
def egg_dropping_recursive_memoized(e  , f):
    if e==1:
        return f
    if f==1 or f ==0:
        return f
    if dp[e][f]!=-1:
        return dp[e][f]
    ans = 9999999
    for k in range(1, f):
        temp = 1 + max(egg_dropping_recursive_memoized(e-1 , k-1) , egg_dropping_recursive_memoized(e , f-k))
        ans = min(ans , temp)
        dp[e][f] = ans
    return dp[e][f]


f = 4
e = 2
print(egg_dropping_recursive_memoized(e , f))
