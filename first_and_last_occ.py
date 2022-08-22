# given a sorted array , find the first and last occurence of an element .
# since the array is sorted , we will use Binary Search
def first_occ(array,ele):
    first=0
    start = 0
    end = len(array)-1
    while start<=end:
        mid = start + (end-start)//2
        
        if array[mid]==ele:
            first = mid
            end = mid-1
        elif ele<array[mid]:
            end = mid-1
        else:
            start = mid+1
    return first


def last_occ(array,ele):
    last=0
    start = 0
    end = len(array)-1
    while start<=end:
        mid = start + (end-start)//2
        
        if array[mid]==ele:
            last = mid
            start = mid+1
        elif ele<array[mid]:
            end = mid-1
        else:
            start = mid+1
    return last

def fnlocc(array , ele):
    first = first_occ(array,ele)
    last = last_occ(array,ele)
    return [first,last]

 
array = [4,10,10,10,10,18,20]
ele = 10
print(fnlocc(array,ele))
