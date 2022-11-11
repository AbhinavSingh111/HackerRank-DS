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
        
#      approach2 : replacing extra 0 in nums1 with the nums2 elements and then sorting using sort func
        for i in range(0,n):
            nums1[i+m]=nums2[i]
        nums1.sort()
        
#      approach3 : replacing extra 0 in nums1 with the nums2 elements and then sorting manually
        for i in range(0,n):
            nums1[i+m]=nums2[i]
        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                if nums1[i]>nums1[j]:
                    nums1[i],nums1[j]=nums1[j],nums1[i]
        
