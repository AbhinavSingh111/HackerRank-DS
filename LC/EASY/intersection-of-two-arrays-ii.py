https://leetcode.com/problems/intersection-of-two-arrays-ii/
  
350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            if i in nums2:
                ans.append(i)
                nums2.remove(i)
        return ans
