695. Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0
        q=[]
        vis=set()
        def bfs(i,j):
            count=1
            q.append((i,j))
            while q:
                print(q)
                i,j = q.pop(0)
                vis.add((i,j))
                for coord in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
                    x,y=coord
                    if x in range(m) and y in range(n) and grid[x][y]==1 and (x,y) not in vis and (x,y) not in q :
                        count+=1
                        q.append((x,y))
            print(count)
            return count


        def dfs(i,j,count):
            vis.add((i,j))
            for coord in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
                x,y=coord
                if x in range(m) and y in range(n) and grid[x][y]==1 and (x,y) not in vis:
                    print(coord)
                    print(count)
                    count+=dfs(x,y,1)
            return count








        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in vis:
                    print((i,j))
                    # area = bfs(i,j)
                    area = dfs(i,j,1)
                    print(area)
                    if area>ans:
                        ans=area
        return ans
