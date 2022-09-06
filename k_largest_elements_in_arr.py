# find the k largest elements in an array

import heapq

def k_smallest(arr , k):
    h = []
    ans=[]
    # heapq._heapify_max(h)
    for i in range(len(arr)):
        h.append(arr[i])
        heapq.heapify(h)
        if len(h)>k:
            heapq.heappop(h)
    while len(h)>0:
        ans.append(heapq.heappop(h))

    return ans


arr=[2,7 ,10 ,4 ,3,20, 15,45]
k=3
print(k_smallest(arr,k))
