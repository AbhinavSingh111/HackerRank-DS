https://leetcode.com/problems/reverse-integer/
7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        temp=x
        rev=0
        if x<0:
            x=x*-1
        while x>0:
            rev = rev*10 + x%10
            x= x//10
        if temp<0:
            rev=rev*-1
            
        #CHECKING IF THE RESULT IS 32 BIT INTEGER OR NOT
        if abs(rev) < 2**31 and rev != 2**31 - 1:
            return rev
        else:
            return 0
