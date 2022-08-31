# find the element which will give minimum difference with key

# here , all we need to understand is that the minimum difference will be 0 and that will be with the key itself
# ie if the key is present , then that ele will give min diff , return that
# otherwise , at the end of bin search , take the index of start and end , and return the min of abs diff bw those 2 ele
# this is because at the end of bin search , the indexes will be pointing to the neighbours of element to be foune ie key , in case the key is not found

# or what we do is find the ceil and floor of key and return the min of abs diff bw them 


# its notthing but binary search
def min_diff_ele(arr, ele):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = start+(end-start)//2
        if arr[mid]==ele:
            return arr[mid]
        elif arr[mid]>ele:
            end = mid-1
        elif arr[mid]<ele:
            start = mid+1
    m1 = abs(arr[start]-ele)
    m2 = abs(arr[end]-ele)
    if m1<m2:
        return arr[start]
    else:
        return arr[end]








arr = [10,20,30,40,50,60,70,80,90]
ele=67
print(min_diff_ele(arr,ele))
