def maxProduct(nums):
    # approach 1
    B=nums[::-1]
    for i in range(1, len(nums)):
        # if nums[i-1]!=0:
            nums[i]*=nums[i-1] or 1
        # if B[i-1]!=0:
            B[i]*= B[i-1] or 1
    return max(nums + B)

    # approach 2
    p=1
    maxi=-999999
    for i in nums:
        p*=i
        maxi=max(p,maxi)
        if p==0:
            p=1
    p=1
    for i in reversed(nums):
        p*=i
        maxi=max(maxi,p)
        if p==0:
            p=1
    return maxi
    
    # approach 3
    N=len(nums)
    max_overall=nums[0]
    max_upto_here=nums[0]
    min_upto_here=nums[0]
    for i in range(1,N):
        temp=max_upto_here
        max_upto_here=max(nums[i],max_upto_here*nums[i],min_upto_here*nums[i])
        min_upto_here=min(nums[i],temp*nums[i],min_upto_here*nums[i])
        max_overall=max(max_overall,max_upto_here)
    return max_overall
nums=[-9,-8,-3,-1,-2,-3,-4,-5,-6,-7,-8,-9,-4]
print(maxProduct(nums))
                
