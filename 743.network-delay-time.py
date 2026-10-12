#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

import heapq
from math import inf
from collections import defaultdict

# @lc code=start


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        dist = [inf] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]
        visited = [False] * (n + 1)

        graph = defaultdict(list)
        for t in times:
            u, v, w = t
            graph[u].append((v, w))

        while heap:
            d, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in graph[u]:
                nd = d + w
                if not visited[v] and nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        max_dist = max(dist[1:])
        return -1 if max_dist == inf else max_dist


# @lc code=end
