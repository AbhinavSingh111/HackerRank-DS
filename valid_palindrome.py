import re
def isPalindrome(s):
    pattern='[A-Za-z0-9]'
    result=re.findall(pattern,s.lower())
    r="".join(result)
    t = r[::-1]
    if r==t:
        return True
    else:
        return False
# or 
    s=s.lower()
    s="".join(filter(str.isalnum,s))
    return(s==s[::-1])

s="A man, a plan, a canal: Panama"
print(isPalindrome(s))
    
        

