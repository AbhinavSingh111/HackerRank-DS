# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

def countSubstrings(s):
    resCount=0
    for i in range(len(s)):
        l,r=i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            resCount+=1
            l-=1
            r+=1
        l,r=i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            resCount+=1
            l-=1
            r+=1
    return resCount
s = "aaa"
# s = "abc"
print(countSubstrings(s))
