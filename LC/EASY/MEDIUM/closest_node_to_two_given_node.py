https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/

2359. Find Closest Node to Given Two Nodes

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(u: int, d: List[int], vis: List[bool], edges: List[int]) -> None:
            # mark it visited
            vis[u] = True
            # check the outgoing edge
            v = edges[u]
            # -1 means there is no outgoing edge, so we skip it
            # if it is visited, we also skip it
            if v != -1 and not vis[v]:
                # the dist going to node v form node u is simply d[u] + 1
                d[v] = d[u] + 1
                # dfs on neigbour node `v`
                dfs(v, d, vis, edges)
        n = len(edges)
        # d1[i]: shortest dist to node i starting from node 1
        # d2[i]: shortest dist to nodes i starting from node 2
        d1, d2 = [float("inf")] * n, [float("inf")] * n
        # vis1[i]: true if node i is visited else false. used for building d1
        # vis2[i]: true if node i is visited else false. used for building d2
        vis1, vis2 = [False] * n, [False] * n
        # dist to node1 from node1 is 0, same as node2 
        d1[node1], d2[node2] = 0, 0
        # build the dist for d1
        dfs(node1, d1, vis1, edges)
        # build the dist for d2
        dfs(node2, d2, vis2, edges)
        # iterate each node to find the min max dist
        ans = -1
        mi = float("inf")
        for i in range(n):
            if max(d1[i], d2[i]) < mi:
                mi = max(d1[i], d2[i])
                ans = i
        return ans
