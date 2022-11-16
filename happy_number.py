HAPPY NUMBER
https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        temp=n
        for i in range(7):
            l=[]
            if n==1:
                return True
            else:
                n=str(n)
                for i in n:
                    l.append( int(i))
                for i in range(len(l)):
                    l[i]=l[i]*l[i]
                n = sum(l)
                if n==temp:
                    return False
        return False
            
            
