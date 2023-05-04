547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/solutions/3480632/union-find-python/
  
  class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: 
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank=[1]*n
        ans=n

        def find(node):
            while node!=parent[node]:
               parent[node]=parent[parent[node]]
               node=parent[node]
            return node

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return 0
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return 1
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    ans-=union(i,j)
        return ans
                
        
       
