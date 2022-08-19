# find the floor of an element in a sorted array
# if the same element is present , return it
# if not , then return the greatest element smaller then it(ie element given)

def floor(arr,ele):
    s = 0
    e = len(arr)-1
    res=0
    while s<=e:
        mid = s+(e-s)//2
        if arr[mid]==ele:
            return arr[mid]
        elif arr[mid]<ele:
            res=arr[mid]
            s=mid+1
        elif arr[mid]>ele:
            e=mid-1
    return res







arr = [1,2,3,4,8,10,12,18,19]
ele = 9
print(floor(arr,ele))
