# find the first occurence of 1 in an infinite sorted  binary array , ie [0,0,0,0,0,0,1,1,1,1,1,1,1,....]

# take low=0 high=1 , keep it in loop while key > arr[high] and make low  = high and high=2*high 
# once we come out of above loop , apply bin sort for finding first occurence of an ele on the current indexes


def first_1_in_inf_arr(arr, ele):
    start = 0
    end = 1
    while ele > arr[end] :
        start = end
        end = 2*end
# binary search to find the first occurence of an element
    while start<=end:
        mid = start+(end-start)//2
        if arr[mid]==ele:
            res = mid
            end = mid-1
        elif arr[mid]>ele:
            end = mid-1

        elif arr[mid]<ele:
            start = mid+1
    return res









arr = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
# the size of array can throw list index out of range , because of limited size of arr while testing
ele=1
print(first_1_in_inf_arr(arr,ele))
