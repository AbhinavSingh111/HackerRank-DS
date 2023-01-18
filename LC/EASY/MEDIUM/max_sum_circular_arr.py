

# kaden's algo
def kd(nums):
    cmx,mmx = -99999,-99999
    cmn,mmn = 99999,99999
    s=0
    for i in nums:
        cmx = max(cmx,0)+i
        mmx = max(mmx,cmx)
        cmn = min(cmn,0)+i
        mmn = min(mmn,cmn)
        s+=i
    return mmx,mmn,s

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums)==0:
            return
        mx , mn , tt = kd(nums)
        # If max subarray sum < 0 then all the numbers in the array are negative. Return the max subarray sum.
        if mx<0:
            return mx

        # here there are 2 cases.
        # 1. either the we can find the max sum while traversing linearly without getting to the circular rotation (kaden's) or..
        # 2. we can find the max sum last part + first part ( ie we are looping circularly)
        # now if we substract the subarray forming the minimum sum from the total sum (we would be left with the sum of last and first part), we could get the array that will give us the max sum 
        # now we need to return the max of the sum we found linearly and this(the one we found for last and the first part ie circular traversal , or we can say suffix and prefix )
        return max(mx , tt-mn)


    





            

            
