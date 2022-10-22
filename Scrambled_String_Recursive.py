# Scrambled String Recursive
# a variation of MCM
# given 2 strings , check if one string is scrambled form of other or not
# we take strings and start to divide them as MCM , 
# there can be 2 conditions , if the divided parts have been swapped or not
# if swapped , compare first part of string 1 with the 2nd part of string 2 and repeat the prochess too check if they are scrampled
# if not swapped , compare first part of string 1 with 1st part of string 2
# if either of these conditions return True then we can say that the strings are scrambled


def cond1(s1 , s2 , n , k):
    if(scrambled_strings_recursive(s1[0:k],s2[n-k:n])==True and scrambled_strings_recursive(s1[k:n],s2[0:n-k])==True):
        return True
    else:
        return False
    
def cond2(s1 , s2 , n , k):
    if(scrambled_strings_recursive(s1[0:k],s2[0:k])==True and scrambled_strings_recursive(s1[n-k:n],s2[n-k:n])==True):
        return True
    else:
        return False

def scrambled_strings_recursive(s1 , s2):
    #  first we will decide the case conditions
    if s1==s2:
        return True
    if len(s1)!=len(s2):
        return False
    if len(s1)<=1:
        return False
    n = len(s1)
    ans = False
    for k in range(1,n):
        if cond1(s1,s2 , n , k ) or cond2(s1,s2 , n , k):
            ans = True
    return ans 
    
s1 = "abhinav"
s2 = "shreyas"
print(scrambled_strings_recursive(s1 , s2))


# memmoized version

dp_map = {}

def cond1(s1 , s2 , n , k):
    if(scrambled_strings_memoized(s1[0:k],s2[n-k:n])==True and scrambled_strings_memoized(s1[k:n],s2[0:n-k])==True):
        return True
    else:
        return False
    
def cond2(s1 , s2 , n , k):
    if(scrambled_strings_memoized(s1[0:k],s2[0:k])==True and scrambled_strings_memoized(s1[n-k:n],s2[n-k:n])==True):
        return True
    else:
        return False

def scrambled_strings_memoized(s1 , s2):
    #  first we will decide the base conditions
    if s1==s2:
        return True
    if len(s1)!=len(s2):
        return False
    if len(s1)<=1:
        return False
    temp = s1
    temp = temp+" "+s2
    if temp in dp_map:
        return dp_map[temp]
    n = len(s1)
    ans = False
    for k in range(1,n):
        if cond1(s1,s2 , n , k ) or cond2(s1,s2 , n , k):
            ans = True
    dp_map[temp] = ans
    return ans 
    
s1 = "abhinav"
s2 = "shreyas_memoized"
print(scrambled_strings_memoized(s1 , s2))
