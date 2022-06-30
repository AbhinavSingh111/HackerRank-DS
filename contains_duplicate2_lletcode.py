# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int):
        if len(list(set(nums)))==len(nums):
            return False
        else:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]==nums[j] and abs(i-j)<=k:
                        return True 
        
