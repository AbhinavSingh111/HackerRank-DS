import numpy
def productExceptSelf( nums) :

    # this approach takes O(n*n) time

    # p=[]
    # for i in range(len(nums)):
    #     if nums[i]!=0 and 0 in nums:
    #         p.append(0)
    #     else :
    #         c=nums[i]
    #         nums[i]=1
    #         p.append(numpy.prod(nums))
    #         nums[i]=c
    # return p



#  this approach takes O(n) time
    right=[1]
    # N=len(nums)
    left=1
    for i in range(len(nums)-1,0,-1):
        right.append(right[-1]*nums[i])
    right=right[::-1]
    for i in range(len(nums)):
        right[i]=right[i]*left
        left*=nums[i]
    return right
A=[3, 1 ,2 ,5 ,3] 

print(productExceptSelf(A))
