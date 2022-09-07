# find the k closest elements of an element in a given array
#  take the difference of elements with given elements and make a max_heap , rest do accordingly and]
# while returning the rest of elements add given element to difference , this way we wont have to store in pairs
# the moment size of heap go beyon k , pop it  and append it to a list
# for the rest of the elements of heap , run a while loop till size and keep popping and appending


# we can easily do this by sorting but that will take best time of n log n , but using heap and this way 
# the time can be reduced to n log k
import heapq

def k_closest(arr , k ,ele):
    h = []
    ans=[]    
    for i in range(len(arr)):
        h.append([abs(ele-arr[i]),arr[i]])
        heapq._heapify_max(h)
        if len(h)>k:
            heapq._heappop_max(h)
    while len(h)>0:
        r=heapq._heappop_max(h)
        ans.append(r[1])
    return ans
        

    


# arr=[6,5,3,2,8,10,9]
arr=[5,6,7,8,9]
k=3
ele = 7
print(k_closest(arr,k , ele))
