212. Word Search II
https://leetcode.com/problems/word-search-ii/solutions/
 
import itertools
class TriNode:
    def __init__(self):
        self.children={}
        self.isWord=False
    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TriNode()
            cur = cur.children[c]
        cur.isWord=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        vis,res = set(),set()
        row , col= len(board),len(board[0])
        root = TriNode()
        for word in words:
            root.addWord(word)
                
        def dfs(r,c,node,word):
            if r<0  or c<0  or r==row or c==col or board[r][c] not in node.children or (r,c) in vis:
                return

            
            node = node.children[board[r][c]]
            word+=board[r][c]
            flag = True
            if node.isWord:
                res.add(word)
                if len(node.children)==0:
                    flag = False
                    del node
            if flag:
                vis.add((r,c))
                dfs(r+1,c,node,word)
                dfs(r,c+1,node,word)
                dfs(r-1,c,node,word)
                dfs(r,c-1,node,word)
                vis.remove((r,c))
        for r,c in itertools.product(range(row),range(col)):
                dfs(r,c,root,"")
        return list(res)


        
