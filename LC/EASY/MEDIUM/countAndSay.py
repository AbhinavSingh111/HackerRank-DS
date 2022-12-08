https://leetcode.com/problems/count-and-say/description/
38. Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:
        # base case
        if n==1:
            return str(1)
        else:
            val = self.countAndSay(n-1)
            op = [1,val[0]]
            i = 0
            while i<len(val)-1:
                if val[i]==val[i+1]:
                    op[-2]+=1
                else:
                    op+=[1,val[i+1]]
                i+=1
            return "".join(str(i) for i in op)
