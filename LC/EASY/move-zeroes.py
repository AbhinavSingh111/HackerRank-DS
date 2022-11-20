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
