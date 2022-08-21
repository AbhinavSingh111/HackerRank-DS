# find the next character in an array of sorted characters

def next_char(arr, ch):
    start = 0
    end = len(arr)-1
    res=''
    while start<=end:
        mid = start+(end-start)//2
        if arr[mid]==ch:
            start = mid+1

        elif arr[mid]>ch:
            res = arr[mid]
            end = mid-1

        elif arr[mid]<ch:
            start = mid+1
    return res









arr = ['a','b','e','g']
ch='f'
print(next_char(arr,ch))
