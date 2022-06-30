class Solution:
    def containsDuplicate(self, nums: List[int]):
        return len(list(set(nums)))<len(nums)
