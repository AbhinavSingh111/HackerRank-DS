# sorting using recursion 
# using I B H 
def insert(arr,temp):
    if len(arr)==0 or arr[-1]<=temp:
        arr.append(temp)
        return
    val = arr[-1]
    arr.pop()
    insert(arr,temp)
    arr.append(val)
    return


def rec_sort(arr):
    if len(arr)==1:
        return 
    temp = arr[-1]
    arr.pop()
    rec_sort(arr)
    insert(arr,temp)
    return arr



arr = [2,6,1,9,4]
print(rec_sort(arr))
