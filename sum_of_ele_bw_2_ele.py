# given an array and 2 ele k1 , k2 .
# find the sum of elements bw k1th smallest and k2th smallest ele

# sifmply use the code of finding kth smallest ele and the put slicing

import heapq
def k_smallest(arr , k):
    h = []
    # heapq._heapify_max(h)
    for i in range(len(arr)):
        h.append(arr[i])
        heapq._heapify_max(h)
        if len(h)>k:
            heapq._heappop_max(h)
    return heapq._heappop_max(h)

def sum_of_ele_bw_2_ele(arr,k1,k2):
    sum=0
    k1 = k_smallest(arr,k1)
    k2 = k_smallest(arr,k2)
    for i in range(len(arr)):
        if arr[i]>k1 and arr[i]<k2:
            sum+=arr[i]
    return sum





arr=[1,3,12,5,15,11]
k1=3
k2=6
print(sum_of_ele_bw_2_ele(arr,k1,k2))
