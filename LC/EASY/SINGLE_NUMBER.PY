https://leetcode.com/problems/single-number/
SINGLE NUMBER

    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)>2:
            i=0
            while i < len(nums):
                temp = nums.pop(i)
                if temp not in nums:
                    return temp
                else:
                    nums.append(temp)                
        else:
            return nums[0]
