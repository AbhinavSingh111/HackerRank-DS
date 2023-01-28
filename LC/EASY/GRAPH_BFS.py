https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1


#User function Template for python3

from typing import List
from queue import Queue
from collections import deque 
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q = deque()
        # append 0th node to queue
        q.append(0)
        # make a visited array with all 0 values
        vis = [0]*V
        # mark 0th node as 1 
        vis[0] = 1
        ans = []
        # till queue exist
        while q: 
            currNode = q.popleft()
            ans.append(currNode)
            # Traverse to each adjacent nodes of currNode
            for neighbours in adj[currNode]:
                # if the neighbour is not visited, then traverse to it
                if not vis[neighbours]:
                    # mark the visited array for the neighbours 1
                    vis[neighbours] = 1
                    # append neighbours to queue 
                    q.append(neighbours)
        return ans

