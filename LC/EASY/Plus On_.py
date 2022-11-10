# https://leetcode.com/problems/plus-one/
66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s+=str(i)
        s=str(int(s)+1)
        digits.clear()
        for i in s:
            digits.append(int(i))
        return digits
