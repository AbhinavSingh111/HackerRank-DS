https://leetcode.com/problems/jump-game/description/
55. Jump Game


RECURSIVE APPROACH

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1: #base case
            return True
        goal = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=goal:
                return self.canJump(nums[0:i+1])
        return False
        















        # goal = len(nums) - 1
        # for i in range(len(nums) - 1 , -1 ,-1):
        #     # i+nums[i] means that we can take this many jumps or can reach upto this index
        #     # while goal is the index we want to reach  , so if the condition meets , we shift the goal post with i
        #     if i+nums[i]>=goal:
        #         goal = i
        # return True if(goal==0) else False


        # try the reachability approach and figure out the recursive , memoized and dp soln
