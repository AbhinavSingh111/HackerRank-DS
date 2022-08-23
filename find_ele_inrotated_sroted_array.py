def count(arr):
    n=len(arr)
    start = 0
    end = n-1
    prev = -1
    next = -1
    # this is one way too to find the min ele
    #     l=0
    # r=len(nums)-1 
    # while l<r:
    #     mid=l+(r-l)//2
    #     if nums[mid]>nums[r]:
    #         l=mid+1
    #     elif nums[mid]<nums[r]:
    #         r=mid
    # return nums[l]
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
def bin(arr,start,end,ele):
    while start<=end:
        mid = start + (end-start)//2
        if arr[mid]==ele:
            return mid
        elif ele<arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1
def element(arr,ele):
    piv = count(arr)
    start=0
    end = len(arr)-1
    l = bin(arr,start,piv-1,ele)
    r = bin(arr,piv,end,ele)
    if l==-1 and r==-1:
        return -1
    elif l==-1:
        return r
    else:
        return l


        


arr = [12,15,18,2,5,6,8,11]
ele = 5
print(element(arr,ele))
