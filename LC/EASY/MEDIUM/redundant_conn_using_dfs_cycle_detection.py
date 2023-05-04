684. Redundant Connection
https://leetcode.com/problems/redundant-connection/solutions/3456908/dfs-cycle-detection-python/
  
  class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(1,len(edges)+1)}
        
        def dfs(n,parent):
            vis.add(n)
            for neigh in graph[n]:
                if neigh in vis and parent!=neigh:
                    return True
                if neigh not in vis:
                    if dfs(neigh , n):
                        return True
    
        for i,j in edges:
            vis=set()
            graph[i].append(j)
            graph[j].append(i)

            if dfs(i,j):
                return [i,j]
            


