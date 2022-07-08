# 1st approach
def findKthLargest(nums, k) :
    nums.sort()
    return nums[len(nums)-k]

#  2nd approach
    maxHeap = nums
    heapq._heapify_max(maxHeap)
    while k > 0:
        x = heapq._heappop_max(maxHeap)
        k-=1
    return x
nums=[2,6,3,8,9,4,5,6,7]
k=2
print(findKthLargest(nums,k))
