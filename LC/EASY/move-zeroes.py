https://leetcode.com/problems/move-zeroes/
Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        dic = {} #KEEP THE RECORD OF NUMBER OF 0s
        for i in nums:
            if i == 0 and i  in dic:
                dic[i]+=1
            elif i==0:
                dic[i]=1
        if 0 in dic: #IF THE LIST HAS ANY 0 THEN REMOVE ALL OF THEM
            for i in range(dic[0]):
                nums.remove(0)
            for i in range(dic[0]): #THEN APPEND THE NUMBER OF 0 PRESENT INITIALLY AT THE END
                nums.append(0)
                
another approach 2 pointers
def moveZeroes(self, nums):
    zero = 0  # records the position of "0"
    for i in xrange(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
