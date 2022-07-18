class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        l=["(","[","{"]
        r=[")","]","}"]
        for i in range(len(s)):
            if s[i] in l:
                stack.append(s[i])
            elif s[i] in r:
                pos=r.index(s[i])
                if len(stack)>0 and l[pos]==stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])      
        return  len(stack)==0
