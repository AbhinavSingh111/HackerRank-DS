LC 1466
Reorder Routes to Make All Paths Lead to the City Zero
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/solutions/3453238/python-dfs/
  
 Intuition
We are given edges that goes from one city to another.
What we can do is make a graph/hash map where we make each node 2 way ie a->b , b->a.

Now we begin a dfs with 0 city.
We check for cities that can visit 0 in graph/hashmap , that is neighbours of 0
Now if we do not have an edge that goes from nieghbour to 0 in our edge list , then we can say that we need to change that edge.

Approach
Make a hashmap where a->b and b->a
Make a visited set
Make a set where we have all the edges given in connections
Run a dfs from 0
In that dfs go to all the neighbours of a city and see if neigh->city exist in our edge list
If not that means we need to change it and hence increase the counter by 1
and add the neigh to visited set and call dfs for neighbour
if neighbour is already visited we continue
In the end we return changes
Complexity
Time complexity:
We traverse all the nodes exactly 1 time

0(n)
Space complexity:
Code
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(node,city) for node,city in connections}
        graph = {i:[] for i in range(n)}
        changes = 0
        vis=set()

        for city,neigh in connections:
            graph[city].append(neigh)
            graph[neigh].append(city)

        def dfs(city):
            nonlocal changes
            for neigh in graph[city]:
                if neigh in vis:
                    continue
                if (neigh,city) not in edges:
                    changes+=1
                vis.add(neigh)
                dfs(neigh)
        vis.add(0)
        dfs(0)
        return changes
        
