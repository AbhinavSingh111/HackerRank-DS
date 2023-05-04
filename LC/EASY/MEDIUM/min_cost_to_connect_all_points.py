1584. Min Cost to Connect All Points
https://leetcode.com/problems/min-cost-to-connect-all-points/description/
  import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        graph = defaultdict(list)
        
        for i, j in itertools.combinations(range(n), 2):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            graph[i].append([dist, j])
            graph[j].append([dist, i])
        res=0
        vis=set()
        heap = [[0,0]]
        while len(vis)<n:
            cost,node = heapq.heappop(heap)
            if node not in vis:
                vis.add(node)
                res+=cost
                for n_cost,n_node in graph[node]:
                    if n_node not in vis:
                        heapq.heappush(heap,([n_cost,n_node]))
        return res
        
            
