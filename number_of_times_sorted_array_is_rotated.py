# find the count of times a sorted array is rotated
# it is equal to the index of min ele
# if ele prev to and next to mid is greater than mid then mid is the min ele
# if not then move to the side where array is not sorted , ie compare mid with start and end
# if mid is greater than start then move to other side and make start=mid+1
# if mid is smaller then start then make end =mid-1
# this is one way too
    # l=0
    # r=len(nums)-1 
    # while l<r:
    #     mid=l+(r-l)//2
    #     if nums[mid]>nums[r]:
    #         l=mid+1
    #     elif nums[mid]<nums[r]:
    #         r=mid
    # return nums[l]

def count(arr):
    n=len(arr)
    start = 0
    end = n-1
    prev = -1
    next = -1
    while start<=end:
        mid = start + (end - start)//2
        prev = (mid+(n)-1)%n
        next = (mid+1)%n
        if arr[mid]<=arr[prev] and arr[mid]<=arr[next]:
            return mid
        elif arr[start]<=arr[mid]:
            start=mid
        elif arr[end]>=arr[mid]:
            end = mid
        


arr = [12,15,18,2,5,6,8,11]
print(count(arr))
