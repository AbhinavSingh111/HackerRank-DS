https://leetcode.com/problems/power-of-three/
POWER OF THREE

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return if n>0 and (math.log10(n)/math.log10(3))%1==0
            return True
        else:
            return False
