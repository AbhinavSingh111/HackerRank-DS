LC 127
WORD LADDER


Intuition
We need to start from the beginWord and reach to endWord in minimum possible steps.

We have few constraints that in each transformation/step only a single letter can be changed.

endWord must be present in wordList.

and each word present is unique.

How is this a graph problem?
We need to consider the words as node and transformation/steps as edges and all the edges are of equal weight.

Hence we need to find the shortest path between beginWord and endWord.

To find the shortest path always think of BFS.
why?
because bfs can do this in polynomial time while dfs will take exponential time.

Approach
Our first priority is to convert the word list into a hashmap/graph where we will use patterns as keys/nodes and all the words matching those patterns as values/neighbours.

we will run a bfs on these nodes.
layer wise(when we need to do a layer wise bfs we run a for loop till the length of queue)

Complexity
Time complexity:
O(N^2*M)
(N is the number of node and M is the lenght of word list)

Space complexity:
Code
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
       
        graph = defaultdict(list)
        
        
        def difference_checker():
            for word in wordList:
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]         
                    graph[pattern].append(word)
        
        difference_checker()


        q=[]
        vis=set()
        

        def bfs():
            count = 1
            q.append(beginWord)
            while q:
                for i in range(len(q)):
                    word=q.pop(0)
                    if word==endWord:
                        return count
                    for j in range(len(word)):
                        pattern = word[:j]+"*"+word[j+1:]
                        for neigh in graph[pattern]:
                            if neigh not in vis:
                                vis.add(neigh)
                                q.append(neigh)
                count+=1
            return 0

        return bfs()
