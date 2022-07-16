# from itertools import permutations
# this approache takes O(n^2)
# def biggestNumber(arr):
#     for i in range(len(arr)):
#         arr[i]=str(arr[i])
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[j]+arr[i]>arr[i]+arr[j]:
#                 arr[j],arr[i]=arr[i],arr[j]
#     s=''.join(arr)
#     return s
    
# this approach takes nlog(n), it uses custom sorting using key 
# import functools
# def myCompare(x, y):
#     o1=x+y
#     o2=y+x
#     if o2>o1:
#         return -1
#     else:
#         return 1	
# def biggestNumber(arr):
#     for i in range(len(arr)):
#         arr[i]=str(arr[i])
#     arr.sort(key=functools.cmp_to_key(myCompare))
#     arr.reverse()   
#     return "".join(arr)

# this approach is 
import functools
def my_cmp_f(a, b):
    if a + b < b + a:
        return -1 
    if a + b > b + a:
        return 1
    return 0
def biggestNumber(arr):
    arr = [str(elem) for elem in arr]
    # arr = sorted(arr, reverse=True)  # 1.56 [time] without this line
    arr = sorted(arr, reverse=True, key=functools.cmp_to_key(my_cmp_f))
    
    result = ''.join(arr)
    
    return result  # 0.79




arr=[9, 5, 34, 30, 3]
print(biggestNumber(arr))
