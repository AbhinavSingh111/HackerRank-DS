79. Word Search

https://leetcode.com/problems/word-search/solutions/3411876/dfs-python/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()
        row,col = len(board),len(board[0])

        if len(word)>row*col:
            return False

        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or r>=row or c<0 or c>=col or board[r][c]!=word[i] or (r,c) in vis:
                return False
            vis.add((r,c))
            for new_r,new_c in ((r+1,c),(r,c+1),(r-1,c),(r,c-1)):
                res = dfs(new_r,new_c,i+1)
                if res:
                    return res
            vis.remove((r,c))
        
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False


    
