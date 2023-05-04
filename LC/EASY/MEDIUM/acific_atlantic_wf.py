417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/description/
 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row=len(heights)
        col=len(heights[0])

        vis,atlantic,pacific=set(),set(),set()
        ans=[]

        def dfs(r,c,vis,prev_height):
# if the island has already been visited or is out of bounds or the height of current island is less than previous traversed island then simply return 
            if (r,c) in vis or r<0 or r==row or c<0 or c==col or heights[r][c]<prev_height:
                return
# else add it to visited
            vis.add((r,c))
# then start traversing towards its neighbours
            for new_r,new_c in ((r+1,c),(r,c+1),(r-1,c),(r,c-1)):
                dfs(new_r,new_c,vis,heights[r][c])

# to check for all the islands from where the water can flow to top edge(pacific) and bottom edge(atlantic)
        for c in range(col):
            # a: pacific ocean
            dfs(0,c,pacific,heights[0][c])
            # b: atlantic
            dfs(row-1,c,atlantic,heights[row-1][c])

# to check for all the islands from where the water can flow to left edge(pacific) and right edge(atlantic)
        for r in range(row):
            # a: atlantic
            dfs(r,col-1,atlantic,heights[r][col-1])
            # a: pacific ocean
            dfs(r,0,pacific,heights[r][0])
        
# taking out the coordinates that can reach both pacific and atlantic 
        for i in atlantic:
            if i in pacific:
                r,c=i
                ans.append([r,c])
        return ans

        
