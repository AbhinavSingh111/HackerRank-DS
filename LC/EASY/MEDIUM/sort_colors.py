https://leetcode.com/problems/sort-colors/description/
75. Sort Colors


# not in place using stacks
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

                       
#      in place
using DNF algo for 0 1 2

        low = 0
        mid = 0
        high = len(nums)-1
        for i in range(len(nums)):
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            
            elif nums[mid]==1:
                mid+=1

            elif nums[mid]==2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
                
