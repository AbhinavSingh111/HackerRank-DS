# find the peak element in a given unsorted array
# here we use the concept of Binary Search on Answer Concept , ie acc to custom conditons for mid ele , and 
# custom conditions for moving either left or right  , we apply binary search 


# here the peak element is the element which is greater than both of its neighbours
# if mid is on the extreme left ie 0 ,  then it should be greater than element at 1 index , otherwise return ele at 1
# if mid is on the extreme right  ie size-1 ,  then it should be greater than element at size-1-1 index , otherwise return ele at size-1-1

# this will return only one peak ele , even if there are more than 1
def peak_ele(arr):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = start+(end-start)//2
        if mid>0 and mid<len(arr)-1:
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]>arr[mid+1]:
                end = mid-1
            elif arr[mid+1]>arr[mid-1]:
                start = mid+1
        elif mid==0:
            if arr[mid]>arr[1]:
                return mid
            else:
                return 1
        elif mid==len(arr)-1:
            if arr[mid]>len(arr)-2:
                return mid
            else:
                return len(arr)-2


arr = [10,20,15,2,23,90,67]
print(peak_ele(arr))
