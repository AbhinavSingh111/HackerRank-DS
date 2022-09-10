# connect the given length of ropes such that the cost of connecting them is minimum
# every time take 2 min lengths and add them , note the cost
# make a min heap of lengths
# pop firsts 2 add them and add it to cost
# push first + second in heap
# repeat it until the length of heap is >=2

import heapq

def connect_rope_to_minimise_cost(h , k ):
    cost=0
    heapq.heapify(h)
    while len(h)>=2:
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        cost +=first + second  
        heapq.heappush(h,(first+second))
    return cost
   
        

    


# arr=[6,5,3,2,8,10,9]
arr=[1,2,3,4,5]
k=2
print(connect_rope_to_minimise_cost(arr,k))
