https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

34. Find First and Last Position of Element in Sorted Array

1: Brute Force , worst case O(n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occ=-1
        last_occ=-1
        for i in range(len(nums)):
            if nums[i]<target:
                continue
            if nums[i] == target:
                if first_occ==-1:
                    first_occ=i
                    last_occ=i
                elif first_occ!=-1:
                    last_occ=i
            if nums[i]>target:
                break
        if first_occ==-1:
            last_occ=-1
        return [first_occ , last_occ]
