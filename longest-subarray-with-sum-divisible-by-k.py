def longSubarrWthSumDivByK (arr,k) : 
	#Complete the function
    n=len(arr)
    c={}
    s=0
    r=0
    ans=0
    c[0]=-1
    for i in range(n):
        s+=arr[i]
        r=s%k
        if r<0:
            r+=k
        if r in c:
            idx=c[r]
            l=i-idx
            if l>ans:
                ans=l
        else:
            c[r]=i
    return ans

arr=[2,7,6,1,4,5]
print(longSubarrWthSumDivByK(arr,3))
