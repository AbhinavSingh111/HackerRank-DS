https://leetcode.com/problems/sort-colors/description/
75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ph = []
        th = []
        for i in range(len(nums)):
            if len(ph)==0:
                ph.append(nums[i])
            else:
                if ph[-1]<=nums[i]:
                    ph.append(nums[i])
                else:
                    while len(ph)>0 and nums[i]<ph[-1]:
                        th.append(ph.pop())
                    ph.append(nums[i])
                    while len(th)!=0:
                        ph.append(th.pop())
