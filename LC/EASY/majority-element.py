   https://leetcode.com/problems/majority-element/
   MAJORITY ELEMENT
   
   def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
                if dic[i]>len(nums)/2:
                    return i
            else:
                dic[i]=1
        return i
#APPROACH 2        
#         since the majority element will be present in more than half of the length , we can simply sort and return the middle element
