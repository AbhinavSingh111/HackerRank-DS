# find the k closest elements to origin  in a given 2d / paired array
#  take the distace using distance formula(root (x2-y2)) use it as key and make a max_heap , rest do accordingly and]
# the moment size of heap go beyon k , pop it  and append it to a list
# for the rest of the elements of heap , run a while loop till size and keep popping and appending


# we can easily do this by sorting but that will take best time of n log n , but using heap and this way 
# the time can be reduced to n log k
import heapq

def k_closest_ele_to_origin(arr , k ):
    h = []
    ans=[]    
    for i in range(len(arr)):
        h.append([(arr[i][0]**2+arr[i][1]**2),[arr[i][0],arr[i][1]]])
        heapq._heapify_max(h)
        if len(h)>k:
            heapq._heappop_max(h)
    while len(h)>0:
        r=heapq._heappop_max(h)
        ans.append(r[1])
    return ans
        

    


# arr=[6,5,3,2,8,10,9]
arr=[[1,3],[-2,2],[5,8],[0,1]]
k=2
print(k_closest_ele_to_origin(arr,k))
