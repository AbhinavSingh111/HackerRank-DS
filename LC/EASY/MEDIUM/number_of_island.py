200. Number of Islands
https://leetcode.com/problems/number-of-islands/submissions/928996576/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        vis=set()
        count=0
        def bfs(rw , cl):
            q=[(rw,cl)]
            while q:
                x,y=q.pop(0)
                if (x,y) in vis:
                    continue
                vis.add((x,y))
                for neigh in ((x+1, y), (x, y+1) , (x-1, y) , (x,y-1)):
                    i,j = neigh
                    if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]) and grid[i][j]=="1":
                        q.append((i,j))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in vis:
                    bfs(i,j)
                    count+=1
        return count



