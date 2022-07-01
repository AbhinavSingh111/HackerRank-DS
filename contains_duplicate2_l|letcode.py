# Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array 
# such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
from bisect import bisect_left,bisect_right
from sortedcontainers import SortedList
def containsNearbyAlmostDuplicate(nums, k, t):
    if t==0 and len(set(nums))==len(nums):
        return False
    if k<0 and t<0:
        return False
    s=SortedList()
    for i,n in enumerate(nums):
        if i>k:s.remove(nums[i-k-1])
        pos1=bisect_left(s,n-t)
        pos2=bisect_right(s,n+t)
        if pos1 != pos2:return True
        s.add(n)
        
    return False
nums=[1,5,9,1,5,9]
k=2
t=3
print(containsNearbyAlmostDuplicate(nums,k,t))
