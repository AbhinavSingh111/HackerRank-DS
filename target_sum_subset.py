class Solution:
    def isSubsetSum (self, N, nums, target):
        dp=[[0 for i in range(target+1)]for i in range(len(nums)+1)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==0 and j==0:
                    dp[i][j]=True  
                elif i==0:
                    dp[i][j]=False  
                elif j==0:
                    dp[i][j]=True  
                else:
                    if dp[i-1][j]==True:
                        dp[i][j]=True  
                    else:
                        val = nums[i-1]
                        if j>=val:
                            if dp[i-1][j-val]==True:
                                dp[i][j]=True
                            else:
                                dp[i][j]=False
                        else:
                            dp[i][j]=False
        return dp[len(nums)][target]
