# print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n
def all_comb(arr , n):
    if n==0:
        return [[]]
    l=[]
    for i in range(len(arr)):
        first=arr[i]
        rem=arr[i+1:]
        comb=all_comb(rem,n-1)
        for x in comb:
            l.append([first]+x)
    return l

arr=[1,2,3,4,5]
n=3
print(all_comb(arr,n))

from itertools import combinations
print(list(combinations([1,2,3,4,5],3)))
