https://leetcode.com/problems/sum-of-two-integers/
371. Sum of Two Integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        
        # works both as while loop and single value check 
        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a
    
    Using logarithm and exponential function
    
    import math
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a==0:
            return b
        if b==0:
            return a
        return int(math.log(exp(a)*exp(b)))
