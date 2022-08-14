#User function Template for python3
from functools import cmp_to_key
def myCompare(x, y):

        o1=x+y
        o2=y+x
        if o2>o1:
            return -1
        else:
            return 1
	
def printLargest(self,arr):
    for i in range(len(arr)):
        arr[i]=str(arr[i])
    arr.sort(key=functools.cmp_to_key(myCompare))
    arr.reverse()   
    return "".join(arr)
