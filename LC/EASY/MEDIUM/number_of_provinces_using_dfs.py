547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/solutions/3480593/dfs-python/
  
  class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: 
        vis = set()
        n = len(isConnected)
        ans= 0

        def dfs(province):
            for neigh in range(len(isConnected[province])):
                if isConnected[province][neigh] and neigh not in vis:
                    vis.add(neigh)
                    dfs(neigh)
        
        for province in range(n):
            if province not in vis:
                vis.add(province)
                ans+=1
                dfs(province)
        return ans
        
       
