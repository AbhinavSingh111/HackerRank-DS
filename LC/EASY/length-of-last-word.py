https://leetcode.com/problems/length-of-last-word/description/
58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        lw=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==" " and lw==1:
                break
            if s[i]==" " and lw==0:
                pass
            else:
                count+=1
                lw=1
        return count
