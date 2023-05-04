LC 463
island perimeter
https://leetcode.com/problems/island-perimeter/solutions/3412222/python-matrix-traversal/



Intuition
We have a grid and we already know that there exist only one 1 island , which means all the lands will be connected.

So if we traverse the whole matrix and whenever we reach a land we add +4 to perimeter because each individual land body will contribute 4 to perimeter and based on if any other land is connected to it and on which side we substract the perimeter by 1.

Approach
Traverse the matrix and whenever you find land , peri+=4
search for lands connected to the current land and depending upon on which sides the current land has a land connected to it do per-=1

return the answer

There are other approaches that you can see in the solutions that follow the same idea but are more efficient.

To me this one looks efficeient enough and easy to get.
Anyhow we will need to traverse the matrix , so there won't be any change in overall time complexity.

Complexity
Time complexity:
O(m*n)
Space complexity:
Code
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        peri=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    peri+=4
                    if  r-1 in range(row) and grid[r-1][c]==1:
                        peri-=1
                    if  c-1 in range(col) and grid[r][c-1]==1:
                        peri-=1
                    if  r+1 in range(row) and grid[r+1][c]==1 :
                        peri-=1
                    if  c+1 in range(col) and grid[r][c+1]==1:
                        peri-=1
        return peri
                
