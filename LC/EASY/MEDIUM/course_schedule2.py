https://leetcode.com/problems/course-schedule-ii/description/

Approach 1: 
  
Intuition
We can conclude that it is a graph problem.
The prerequisites/dependency denotes the directed edges.
Here with the word "dependency" we might be able to think topological sort (u-->v , for v to happen u should come before v).
Here we need to print the order , so we will use topological sort.
This can also be done by making some changes in LC 210
Since Topological sort works only on DAGs , we need to modify our code to account for cycles
Approach
we convert our prerequisite list into adjacency list , to keep tracke of the neighbours of all the nodes
Rest is mentioned in comments.
Complexity
Time complexity:
O(v+e) , v is vertices/nodes/cources , e is edges.
Space complexity:
Code
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g={i:[] for i in range(numCourses)}
        for i in prerequisites:
            g[i[0]].append(i[1])
 
        vis,cycle=set(),set()
        st=[]
        def dfs(curr):
            # we need to check if the course we are visiting is already present in cycle set , if yes that means we encountered a cycle and 
            # we return false
            if curr in cycle:
                return False
            # if the course has already been visited , we do not want to visit it again so we return True from here
            if curr in vis:
                return True
            # if both the above cond are false , we add the course to our cycle set , to keep track of cyckes
            cycle.add(curr)
            for neigh in g[curr]:
                # if our dfs returns false , that means we enountered cycle , so we also return false
                if dfs(neigh)==False:
                    return False
            # if we do not enounter any cycle in that course path , we remove that course from cycle set , because we are no more going that 
            # path
            cycle.remove(curr)
            # since we have not enountered any cycle , that means we can visit/complete this course , hence we add this to visited/completed
            #set
            vis.add(curr)
            # add the course to our ans
            st.append(curr)
            # we know that we can take this course , so we return True
            return True
    
        for i in range(numCourses):
            # if our dfs returns false we return empty array
            if not dfs(i):return []
        # else we return our answer array
        return st
##############################################################################################################################################################
      Approach 2:
        
        
        Intuition
This question is same as LC 210.
LC 210 Course Schedule explanation
we need to make slight changes in order to incorporate the order.

Approach
Everytime True is returned in our code , we know that a course can be visited , so we add it in our output list.

Complexity
Time complexity:
O(v+e)
Space complexity:
Code
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g={i:[] for i in range(numCourses)}
        for i in prerequisites:
            g[i[0]].append(i[1])
        print(g)
        vis=set()
        st=[]
        def dfs(curr):
            if curr in vis:
                return False
            if g[curr]==[]:
                if curr not in st:
                    st.append(curr)
                return True
            vis.add(curr)
            for neigh in g[curr]:
                if not dfs(neigh):return False
            vis.remove(curr)
            g[curr]=[]
            if curr not in st:
                st.append(curr)
            return True
        for i in range(numCourses):
            if not dfs(i):return []
        return st
