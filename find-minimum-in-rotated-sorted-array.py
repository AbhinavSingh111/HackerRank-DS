class Solution:
    def findMin(self, nums: List[int]) -> int:
#       approach 1
        # return min(nums)
#         approach 2
        # b=nums[0]
        # for i in range(1,len(nums)):
        #     if nums[i-1]<=nums[i]:
        #         continue
        #     else:
        #         return nums[i]
        # return b
    
#        recursive approach
        # if l==r:
        #     return nums[l]
        # mid=l+(l-r)//2
        # if nums[mid]>nums[r]:
        #     return self.findMin(nums,mid+1,r)
        # if nums[mid]<nums[r]:
        #     return self.findMin(nums,l,mid)
        # return nums[r]
        
#         iterative approach 
        l=0
        r=len(nums)-1 
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]<nums[r]:
                r=mid
        return nums[l]
        
        
                
            
        
