 https://leetcode.com/problems/merge-sorted-array/
  Merge Sorted Array
  
      def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#       approach 1 : eliminating the extra 0's in nums1 and then adding nums2 and sorting 
        i=0
        while i<len(nums1):
            if i<m:
                i+=1
            else:
                nums1.pop(i)
        nums1+=nums2
        nums1.sort()
