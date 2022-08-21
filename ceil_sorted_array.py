# find the ceil of an element in a sorted array
# if the same element is present , return it
# if not , then return the smallest element grater  than it(ie element given)

def ceil(arr,ele):
    s = 0
    e = len(arr)-1
    res=0
    while s<=e:
        mid = s+(e-s)//2
        if arr[mid]==ele:
            return arr[mid]
        elif arr[mid]<ele:
            s=mid+1
        elif arr[mid]>ele:
            res=arr[mid]
            e=mid-1
    return res







arr = [1,2,3,4,8,10,12,18,19]
ele = 15
print(ceil(arr,ele))
