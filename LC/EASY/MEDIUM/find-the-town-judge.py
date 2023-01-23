https://leetcode.com/problems/find-the-town-judge/description/
997. Find the Town Judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if n<=1:
        #     return 1
        # possible_judge = {}
        # for i in range(len(trust)):
        #     if trust[i][1] in possible_judge:
        #         possible_judge[trust[i][1]]+=[trust[i][0]]
        #     else:
        #         possible_judge[trust[i][1]]=[trust[i][0]]
        # pj = 0
        # for i in possible_judge:
        #     temp = sorted(possible_judge[i])
        #     if i not in temp and len (temp)==n-1:
        #         pj = i
        #     if pj  in temp:
        #         return -1
        # if pj!=0:
        #     return pj
        # else:
        #     return -1

        # Count the number of people this guy is being trusted by.
        beingTrustedBy = defaultdict(int)
        # Count the number of people this guy trusts
        trusting = defaultdict(int)
        
        # Going through the trust relations.
        for a,b in trust:
            trusting[a] += 1
            beingTrustedBy[b] += 1
        
        # The judge trusting 0 people, and being trusted by n-1 people
        for i in range(1,n+1):
            if beingTrustedBy[i] == n-1 and trusting[i] == 0:
                return i
        
        # Didn't find a judge
        return -1
            





        l=[]
        # for i in possible_judge:
        #     l.append(possible_judge[i])
        # if l:
        #     t=l[0]
        #     print(t)
        # else:
        #     return -1
        # for i in l[1:]:
        #     t = [val for val in t if val in i]
        #     print(t)


        # print(t)
        # if t:  
        #     return t[0]
        # else:
        #     return -1
            
        print(possible_judge)

        
        
