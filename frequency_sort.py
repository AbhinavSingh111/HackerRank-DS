# implement frequency sort
# use hash map / dict to get the frequency of elements 
# use min heap or max heap as per sorting manner , m store freq , and ele in pair
# the moment size of heap go beyon k , pop it  and append it to a list
# for the rest of the elements of heap , run a while loop till size and keep popping and appending


# we can easily do this by sorting but that will take best time of n log n , but using heap and this way 
# the time can be reduced to n log k
import heapq

def frequency_sort(arr):
    frequency = {}
    h=[]
    ans=[]    
    for i in range(len(arr)):
        if arr[i] in frequency:
            frequency[arr[i]]+=1
        else:
            frequency[arr[i]]=1
    for i in frequency.items():
        h.append([i[0],i[1]])
        heapq.heapify(h)
    while len(h)>0:
        freq = h[0][1]
        ele  = h[0][0]
        for i in range(freq):
            ans.append(ele)
        heapq.heappop(h)
    return ans
        

    


# arr=[6,5,3,2,8,10,9]
arr=[4,3,1,2,2,1,1]
print(frequency_sort(arr))
