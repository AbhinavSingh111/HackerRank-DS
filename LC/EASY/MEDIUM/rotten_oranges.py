https://leetcode.com/problems/rotting-oranges/solutions/3313130/bfs-with-explanation/
  
Intuition
we can see that the grid is acting as a graph , we need to visit its adjacent nodes.
So a graph traversal algorithm will work.
Here we are using BFS.

Approach
As we can see that we need to only visit the nodes that have 1 in them.
So what we can do is that we seperate the coordinates in a list that we need to visit , i.e that have 1 and put the coordinates that have 2 in queue(initially (0,0)).

Since we need to visit the adjacent neighbours we can visit 4 cordinates for each node.

we will check if any of those coordinates are present in our list of coordinates that we need to visit , if yes , then we remove those coordinates from our list and add them to queue assumming that they are rotten now.

we will use a for loop with the length of queue and each time the for loop ends we increase the count(minute by 1)

in the end if we have any coordinate left to visit in our list then that means all the oranges will not rot and we return -1

else we return the count.

Complexity
Time complexity:
O(v+e)

Space complexity:
Code
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count=0
        q=[]
        v=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    v.append((i,j))    
        print(q,v)    
        while q and v: 
            print(q)  
            for _ in range(len(q)):
                i,j = q.pop(0)
                for coord in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
                    if coord in v:
                        v.remove(coord)
                        q.append(coord)
            count+=1
        return -1 if v else count
