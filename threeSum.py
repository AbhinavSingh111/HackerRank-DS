def threeSum(nums):
#         nums.sort()
#         N=len(nums)
#         if N<3:
#             return o
#         o=[]

#         for i in range(N):
#             if i!=0 and nums[i]==nums[i-1]:
#                 continue
#             target=-nums[i]
#             p=twoSum(nums,i+1,N-1,target) 
#             for j in p:
#                 j.append(nums[i])
#                 o.append(j)


#         return o
# def twoSum(nums,si,hi,target):
#     l=si
#     h=hi
#     o=[]
#     while l<h:
#         if l!=si and nums[l]==nums[l-1]:
#             l+=1
#             continue
#         s=nums[l]+nums[h]
#         if s==target:
#             p=[]
#             p.append(nums[l])
#             p.append(nums[h])
#             o.append(p)
#             l+=1
#             h-=1
#         elif s>target:
#             h-=1
#         elif s<target:
#             l+=1
#     return o
    #         in one function
        nums.sort()
        N=len(nums)
        o=[]
        for i in range(N):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            l=i+1
            h=N-1
#             using 2 sum approach
            while l<h:
                if l!=i+1 and nums[l]==nums[l-1]:
                    l+=1
                    continue
                s=nums[l]+nums[h]
                if s==target:
                    o.append([nums[i],nums[l],nums[h]])
                    l+=1
                    h-=1
                elif s<target:
                    l+=1
                elif s>target:
                    h-=1
        return o
nums= [1,2,-2,-1]
print(threeSum(nums))
