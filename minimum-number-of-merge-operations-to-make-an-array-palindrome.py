def turnIntoPalindrome(arr):
    count=0
    i=0
    j=len(arr)-1
    p=[]
    while i<j:
        if arr[i]==arr[j]:
            i+=1
            j-=1
        elif arr[i]<arr[j]:
            i+=1
            arr[i]+=arr[i-1]
            count+=1
            arr.remove(arr[i-1])
            i=0
            j=len(arr)-1
        else:
            j-=1
            arr[j]+=arr[j+1]
            count+=1
            arr.remove(arr[j+1])
            i=0
            j=len(arr)-1
    p.append([arr,count])
    return p



# arr=[11,14,15,99]
# arr=[1,4,5,1]
# arr=[1,5,1]
arr=[]

print(turnIntoPalindrome(arr))
