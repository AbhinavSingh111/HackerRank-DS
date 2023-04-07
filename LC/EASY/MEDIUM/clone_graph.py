LC-133
https://leetcode.com/problems/clone-graph/submissions/929629873/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldNode={}

        def dfs(node):
            if node in oldNode:
                return oldNode[node]

            copy = Node(node.val)
            oldNode[node] = copy

            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            return copy
        return dfs(node) if node else None
