743. Network Delay Time
https://leetcode.com/problems/network-delay-time/solutions/3362208/dijkstra-with-explanation/

import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph=defaultdict(list)
        for source , target , time in times:
            graph[source].append((target,time))

        time_needed=[float('inf')]*n
        time_needed[k-1]=0
        heap=[(0,k)]

        while heap:
            time,node=heapq.heappop(heap)
            for neigh , neigh_time in graph[node]:
                new_time=time+neigh_time
                if new_time<time_needed[neigh-1]:
                    time_needed[neigh-1]=new_time
                    heapq.heappush(heap,(new_time,neigh))
        return -1 if float('inf') in time_needed else  max(time_needed)
