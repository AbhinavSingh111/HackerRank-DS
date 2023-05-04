LC 463
Island Perimeter
https://leetcode.com/problems/island-perimeter/solutions/3412244/bfs-python/

Intuition
There are better approaches but this one came to me first.

This problem resembles island counts problem.

We have interconnected land that forms an island and we have only one island.

So we begin with the first land and run a graph traversal algo bfs or dfs , any will work.

I am using BFS.

you go to the land and start looking for its neighbours if the neighbours are out of bound that means water so we add 1 to perimeter.

if the neighbour in itself is water we again increment the perimeter by 1

if the neighbour is a land add it to queue.

Approach
Run a BFS begining from the first land.

if the neighbours are out of bound that means water so we add 1 to perimeter.

if the neighbour in itself is water we again increment the perimeter by 1

if the neighbour is a land add it to queue.

Complexity
Time complexity:
O(M+N)

Space complexity:
Code
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        vis=set()
        q=[]
       
        def bfs(r,c):
            peri=0
            q.append((r,c))
            while q:
                r,c=q.pop(0)
                vis.add((r,c))
                for neigh in ((r+1,c),(r,c+1),(r-1,c),(r,c-1)):    
                    new_r,new_c = neigh
                    if new_r not in range(row) or new_c not in range(col):
                        peri+=1                    
                    elif grid[new_r][new_c]==0:
                        peri+=1                       
                    elif (new_r,new_c) not in vis and (new_r,new_c) not in q:
                        q.append((new_r,new_c))
            return peri
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    return bfs(r,c)
            
