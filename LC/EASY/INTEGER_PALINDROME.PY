https://leetcode.com/problems/palindrome-number/
9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x)==str(x)[::-1]
        if x<0 or (x%10==0 and x!=0):
            return False
        elif x<=0 or x<10:
            return True
        else:
            temp=x
            rev=0
            while x>0:
                rev = rev*10 + x%10
                x= x//10
            return temp==rev
