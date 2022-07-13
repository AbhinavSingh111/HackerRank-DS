# approach 1 using quick select
def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j :
        while  i<len(arr) and arr[i]<=pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[low],arr[j]=arr[j],arr[low]
    return j


def kthElement(arr,low,high,k):
    p=partition(arr,low,high)
    if p==k:
        return arr[k]
    elif p>k:
        return kthElement(arr,low,p-1,k)
    else:
        return kthElement(arr,p+1,high,k)

arr=[7 ,10 ,4 ,20, 15]
k=4
print(kthElement(arr,0,len(arr)-1,k-1))


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


