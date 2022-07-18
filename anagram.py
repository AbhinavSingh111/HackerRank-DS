from itertools import permutations
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#       this approach is heavy and overkill , time consuming
        # l=[list(i) for i in permutations(s)]
        # if list(t) in l:
        #     return True
        # else:
        #     return False
        s=list(s)
        t=list(t)
        if len(s)!=len(t):
            return False
        for i in s:
            if i in t:
                idx=t.index(i)
                t.remove(t[idx])
        if len(t)==0:
            return True
        else:
            return False
#           other approach is usiing counter
        return Counter(s)==Counter(t)
