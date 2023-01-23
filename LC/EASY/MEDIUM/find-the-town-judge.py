https://leetcode.com/problems/find-the-town-judge/description/
997. Find the Town Judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

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
    
 APPROACH 2

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
<!-- the base condition -->
        if n<=1:
            return 1
<!-- a hash map.
Keep person being trusted as the key and the person trusting as values. -->
        possible_judge = {}
        for i in range(len(trust)):
            if trust[i][1] in possible_judge:
                possible_judge[trust[i][1]]+=[trust[i][0]]
            else:
                possible_judge[trust[i][1]]=[trust[i][0]]
        pj = 0
<!-- list to store remaining values/persons -->
        l=[]
        for i in possible_judge:
            temp = possible_judge[i]
<!-- if the key(ie possible judge is not in the list of people who trusts him and the number of those people should be 1 less than total number of people and there needs to exist only one such person) -->
            if i not in temp and len (temp)==n-1 and pj==0:
                pj = i
            else:
<!-- if the above cond does not match add the people in a seperate list -->
                l+=temp

<!-- if we have found a possible judge and that possible judje is not in the list of people who trusts him then return pj -->
        if pj!=0 and pj not in l:
            return pj
        else:
            return -1

        
        
            

        
        
