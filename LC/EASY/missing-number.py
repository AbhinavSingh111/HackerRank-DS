Missing Number
https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         we take the sum of all the elements in that range and substract it with the sum of given elements . the difference is our answer
        return sum(range(0,len(nums)+1))-sum(nums)
