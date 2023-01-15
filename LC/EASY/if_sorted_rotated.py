https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/submissions/

1752. Check if Array Is Sorted and Rotated

class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(1 , len(nums)):
            # if previous element is greater than current , that means it is the point of discontinuation
            if  nums[i-1]>nums[i]:
                # from the point of discontinuation we do list slicing to form the array and if that matches the orignal sorted array , then true else false
                return nums[i:]+nums[0:i]==sorted(nums)      
        return True



