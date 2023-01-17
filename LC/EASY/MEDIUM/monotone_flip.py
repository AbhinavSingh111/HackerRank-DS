https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
    
33. Search in Rotated Sorted Array

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # ans , one = 0 , 0
        # for i in s:
        #     # looking for 1s 
        #     if i=="1":
        #         one+=1
        #     # this will execute only if we have found the first occurence of 1 
        #     elif one:
        #         one-=1
        #         ans+=1
        # return ans
        one , zero = 0 , 0
        for i in s:
            if i=="1":
                one+=1
            elif one:
                zero+=1
            zero=min(one,zero)
        return zero
