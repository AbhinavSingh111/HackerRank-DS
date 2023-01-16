33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

def min_ele(nums):
    start=0
    end = len(nums)-1
    while start<end:
        mid = (start+end)//2
        if nums[mid]>nums[end]:
            start = mid+1
        elif nums[mid]<nums[end]:
            end = mid
    return start

def bs(l,r,arr, tgt):
    while l<=r:
        mid = (l+r)//2
        if arr[mid]==tgt:
            return mid
        elif tgt>arr[mid]:
            l=mid+1
        elif tgt<arr[mid]:
            r = mid-1
    return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mini =  min_ele(nums)
        l = bs(0,mini-1,nums,target)
        r = bs(mini,len(nums)-1,nums,target)
        if l!=-1:
            return l
        else:
            return r
