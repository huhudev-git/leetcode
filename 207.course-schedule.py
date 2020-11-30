#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

from typing import List

UNSEARCH = 0
SEARCHING = 1
SEARCHED = 2


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        prerequisites
        1 -> 0, 1 depend on 0
        """
        graph = [[] for _ in range(numCourses)]
        visit = [UNSEARCH for _ in range(numCourses)]
        for p in prerequisites:
            start = p[0]
            end = p[1]
            graph[start].append(end)

        for i in range(numCourses):
            if (visit[i] == UNSEARCH) and (not self.dfs(graph, i, visit)):
                return False
        return True

    def dfs(self, graph, node, visit):
        visit[node] = SEARCHING
        # connect
        for c in graph[node]:
            # use dfs
            if visit[c] == UNSEARCH:
                # dfs return false only visit[c] == SEARCHING
                if not self.dfs(graph, c, visit):
                    return False
            # if we find SEARCHING node -> here is circle
            elif visit[c] == SEARCHING:
                return False
        # this node finished
        visit[node] = SEARCHED
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))
# @lc code=end
