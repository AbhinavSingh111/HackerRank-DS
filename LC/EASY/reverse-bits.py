https://leetcode.com/problems/reverse-bits/submissions/
190. Reverse Bits


class Solution:
    def reverseBits(self, n: int) -> int:
        # bin_n = format(n, 'b').zfill(32)
        # ans = int(bin_n[::-1], 2)
        # return ans
    
    
    #xrange does not work in python 3
        ans = 0
        for i in xrange(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans
