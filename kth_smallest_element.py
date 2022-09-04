# approach 1 using quick select

# check this appprach as this seems not working
# def partition(arr,low,high):
#     pivot=arr[low]
#     i=low
#     j=high
#     while i<j :
#         while  i<len(arr) and arr[i]<=pivot:
#             i+=1
#         while arr[j]>pivot:
#             j-=1
#         if(i<j):
#             arr[i],arr[j]=arr[j],arr[i]
    
#     arr[low],arr[j]=arr[j],arr[low]
#     return j


# def kthElement(arr,low,high,k):
#     p=partition(arr,low,high)
#     if p==k:
#         return arr[k]
#     elif p>k:
#         return kthElement(arr,low,p-1,k)
#     else:
#         return kthElement(arr,p+1,high,k)

# arr=[7 ,10 ,4 ,20, 15]
# k=4
# print(kthElement(arr,0,len(arr)-1,k-1))


# direct/brute
def partition(arr,k):
     arr.sort()
     return(arr[k-1])
arr=[7 ,10 ,4 ,20, 15]
k=4
print(kthElement(arr,k-1))


# using hwapify

def partition(arr,k):
    heapq.heapify(arr)
    while k>0:
        r = heapq.heappop(arr)
        k-=1
    return r

arr=[7 ,10 ,4 ,20, 15]
k=4
print(kthElement(arr,k-1))


# another heapify app roach using max heap
# this approach uses heap
# here we have to find smallest ele , so we make max heap
# we declare a max heap and then run a for loop over array
# we keep pushing the elements in heap and keep checking the size of heap
# the instance the size of heap gets bigger than k , pop the topmost ele , as it cant be our ans
# return the topmost ele at the end


# import heapq
# listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
# heapq.heapify(listForTree)             # for a min heap
# heapq._heapify_max(listForTree)        # for a maxheap!!
# If you then want to pop elements, use:

# heapq.heappop(minheap)      # pop from minheap
# heapq._heappop_max(maxheap) # pop from maxheap

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


arr=[2,7 ,10 ,4 ,3,20, 15]
k=3
print(k_smallest(arr,k))


