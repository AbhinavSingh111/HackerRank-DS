def twoSum(nums,target):
    nums.sort()
    l=0
    h=len(nums)-1
    o=[]
    while l<h:
        if l!=0 and nums[l]==nums[l-1]:
            l+=1
            continue
        s=nums[l]+nums[h]
        if s==target:
            o.append([nums[l],nums[h]])
            l+=1
            h-=1
        elif s>target:
            h-=1
        elif s<target:
            l+=1
    return o
nums=[1,2,-2,-1]
print(twoSum(nums,10))
