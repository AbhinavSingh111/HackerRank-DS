# search an element in an infinite array

# take low=0 high=1 , keep it in loop while key > arr[high] and make low  = high and high=2*high 
# once we come out of above loop , apply bin sort on the current indexes


def ele_in_inf_arrchar(arr, ele):
    start = 0
    end = 1
    while ele > arr[end] :
        start = end
        end = 2*end
    
    while start<=end:
        mid = start+(end-start)//2
        if arr[mid]==ele:
            return mid

        elif arr[mid]>ele:
            end = mid-1

        elif arr[mid]<ele:
            start = mid+1
    return "NOT PRESENT"









arr = [10,20,30,40,50,60,70,80,90]
# the size of array can throw list index out of range , because of limited size of arr while testing
ele=70
print(ele_in_inf_arrchar(arr,ele))
