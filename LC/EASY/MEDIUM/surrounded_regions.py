130. Surrounded Regions
https://leetcode.com/problems/surrounded-regions/solutions/3508636/dfs-python-with-explanation/?orderBy=newest_to_oldest
  
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row,col = len(board),len(board[0])
        vis=set()

        def dfs(r,c):
            board[r][c]="U"
            vis.add((r,c))
            for new_r,new_c in ((r+1,c),(r,c+1),(r-1,c),(r,c-1)):
                if new_r in range(row) and new_c in range(col) and board[new_r][new_c]=="O" and (new_r,new_c) not in vis:
                    dfs(new_r,new_c)


        for r,c in itertools.product(range(row),range(col)):
            if r in [0,row-1] or c in [0,col-1]:
                if board[r][c]=="O" and (r,c) not in vis:
                    dfs(r,c)
        print(board)
        for r,c in itertools.product(range(row),range(col)):
            if board[r][c]=="U":
                board[r][c]="O"
            else:
                board[r][c]="X"
