# find the k most frequent elements  in a given array
# use hash map / dict to get the frequency of elements 
# use min heap m store freq , and ele in pair
# the moment size of heap go beyon k , pop it  and append it to a list
# for the rest of the elements of heap , run a while loop till size and keep popping and appending


# we can easily do this by sorting but that will take best time of n log n , but using heap and this way 
# the time can be reduced to n log k
import heapq

def k_top_frequent(arr , k ):
    frequency = {}
    h=[]
    ans=[]    
    for i in range(len(arr)):
        if arr[i] in frequency:
            frequency[arr[i]]+=1
        else:
            frequency[arr[i]]=1
    for i in frequency.items():
        h.append([i[1],i[0]])
        heapq.heapify(h)
        if len(h)>k:
            heapq.heappop(h)
    while len(h)>0:
        r=heapq.heappop(h)
        ans.append(r[0])
    return ans
        

    


# arr=[6,5,3,2,8,10,9]
arr=[1,1,1,3,2,2,4]
k=2
print(k_top_frequent(arr,k ))
