# sort a given k sorted / nearly sorted  array
#  fa nearly/ k sorted array is defined such that the acutal position of an element is either k side to the left or k side to the right
# make a min  heap
# the moment size of heap go beyon k , pop it  and append it to a list
# for the rest of the elements of heap , run a while loop till size and keep popping and appending


# we can easily do this by sorting but that will take best time of n log n , but using heap and this way 
# the time can be reduced to n log k
import heapq

def k_smallest(arr , k):
    h = []
    ans=[]
    # heapq._heapify_max(h)
    for i in range(len(arr)):
        h.append(arr[i])
        heapq.heapify(h)
        if len(h)>k:
            ans.append(heapq.heappop(h))
    while len(h)>0:
        ans.append(heapq.heappop(h))

    return ans


arr=[6,5,3,2,8,10,9]
k=3
print(k_smallest(arr,k))
