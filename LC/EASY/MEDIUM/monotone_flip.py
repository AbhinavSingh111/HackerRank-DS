https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
    
926. Flip String to Monotone Increasing


# both works 

the idea is to start counting from first occurence of one because all the 0 s before that need not be changed they can be ignored.
not use 2 variables each for the occurence of 1 and 0 and increase the counter ,
with every iteration change the value of variiable containing 0s to the  min(v0,v1)


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
