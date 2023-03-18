https://leetcode.com/problems/all-paths-from-source-to-target/post-solution/
  
  
class Solution: 
    def modified_dsa(self ,curr ,  graph , visited , target , path, ls ):
        if curr==target:
            print(path)
            ls.append(path)
            return 
        
        for neighbour in graph[curr]:
            print(neighbour)
            if visited[curr]==False:
                visited[curr]=True
                self.modified_dsa(neighbour , graph , visited , target , path+[neighbour] ,ls)
                visited[curr]=False


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ls=[]
        visited=[False for i in range(len(graph))]
        self.modified_dsa(0 , graph , visited , len(graph)-1 , [0] ,ls)
        return ls




        
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        temp =[0]
        def dfs(currNode , path):
            if currNode == len(graph)-1:
                ans.append(path)
                return
            for neighbour in graph[currNode]:
                if neighbour not in temp:
                    temp.append(neighbour)
                    dfs(neighbour , path+[neighbour])
                    temp.remove(neighbour)
        dfs(0,[0])
        return ans
