332. Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/solutions/3512764/dfs-python-with-explanation/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph={src:[] for src,dest in tickets}

        for src, dest in tickets:
            graph[src].append(dest)
        
        res=["JFK"]
        def dfs(src):
            if len(res)==len(tickets)+1:
                return True

            if src not in graph:
                return False

            temp = graph[src].copy()
            for i , v in enumerate(temp):
                graph[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                graph[src].insert(i,v)
                res.pop()
            return False
        if dfs("JFK"):
            return res
