https://leetcode.com/problems/single-number/
SINGLE NUMBER

    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)>2:
            i=0
            while i < len(nums):
                temp = nums.pop(i)
                if temp not in nums:
                    return temp
                else:
                    nums.append(temp)                
        else:
            return nums[0]
        
#         APPROACH 2

                dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic:
            if dic[i]==1:
                return i
