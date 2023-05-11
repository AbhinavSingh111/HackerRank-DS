778. Swim in Rising Water
https://leetcode.com/problems/swim-in-rising-water/solutions/3512481/dijkstra-modified-python/
  
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        vis=set()
        time = 0
        n = len(grid)
        heap = heapq
        heap = [[grid[0][0],0,0]]
        vis.add((0,0))
        while heap:
            t,i,j = heapq.heappop(heap)
            if i==n-1 and j ==n-1:
                return t
            
            for coord in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
                new_i,new_j =coord
                if new_i in range(n) and new_j in range(n) and coord not in vis:
                    vis.add((new_i,new_j))
                    heapq.heappush(heap,(max(t,grid[new_i][new_j]),new_i,new_j))
        return time
