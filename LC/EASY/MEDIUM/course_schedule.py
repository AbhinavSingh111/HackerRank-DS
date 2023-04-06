https://leetcode.com/problems/course-schedule/description/
  
  
Intuition
1.We can conclude that it is a graph problem.
2.The prerequisites/dependency denotes the directed edges.
3.Here with the word "dependency" we might be able to think topological sort (u-->v , for v to happen u should come before v). We can use it too. But the point is , we can use topological sorts in DAGs only.
4.Here in the second example we can see a cycle forming, so it might get a bit tricky to implement topological sort.

Here I am using DFS with some modifications required by question.

Approach

1.Convert the prerequisite edge list into a hash map.

2.The keys with empty lsit will denote that they have no prerequisites/conditions so they can be completed.

3.We use 2 base conditions -- 
  (a). If the node/course we are visiting / trying to finish is already finished / visited then we return False.
  (b).If the course we are visiting has no prerequisites , then we return True.

4.We follow normal dfs beyond this point.

5.We run the dfs for all the nodes assuming that we also might enounter unconnected components.


Complexity

Time complexity:
O(n+e)



Code
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g={i:[] for i in range(numCourses)}
        for i in prerequisites:
            g[i[0]].append(i[1])
        print(g)
        vis=set()
        def dfs(curr):
            if curr in vis:
                return False
            if g[curr]==[]:
                return True
            vis.add(curr)
            for neigh in g[curr]:
                if not dfs(neigh):return False
            vis.remove(curr)
            g[curr]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):return False
        return True
