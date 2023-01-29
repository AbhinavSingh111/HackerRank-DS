class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        ans = []
        def dfs(currNode):
            if currNode not in ans:
                ans.append(currNode)
                for neighbours in adj[currNode]:
                    dfs(neighbours)
  
        dfs(0)
        return ans
