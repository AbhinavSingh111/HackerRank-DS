https://leetcode.com/problems/remove-duplicates-from-sorted-array/
26. Remove Duplicates from Sorted Array

def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i <= len(nums)-1:
            if i==len(nums)-1:
                break
            elif nums[i]==nums[i+1]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
