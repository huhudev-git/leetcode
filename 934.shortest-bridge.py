#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start
from typing import List


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        """
        DFS, BFS
        """
        m = len(A)
        n = len(A[0])

        island1 = []
        for row in range(m):
            if island1:
                break
            for col in range(n):
                if A[row][col]:
                    self.dfs(A, island1, row, col)
                    break

        distance = -1
        while island1:
            distance += 1
            n = len(island1)

            for _ in range(n):
                cell = island1.pop(0)
                row, col = cell[0], cell[1]

                if row > 0:
                    if A[row - 1][col] == 0:
                        island1.append([row - 1, col])
                        A[row - 1][col] = 2
                    elif A[row - 1][col] == 1:
                        return distance
                if col > 0:
                    if A[row][col - 1] == 0:
                        island1.append([row, col - 1])
                        A[row][col - 1] = 2
                    if A[row][col - 1] == 1:
                        return distance
                if row < len(A) - 1:
                    if A[row + 1][col] == 0:
                        island1.append([row + 1, col])
                        A[row + 1][col] = 2
                    if A[row + 1][col] == 1:
                        return distance
                if col < len(A[0]) - 1:
                    if A[row][col + 1] == 0:
                        island1.append([row, col + 1])
                        A[row][col + 1] = 2
                    if A[row][col + 1] == 1:
                        return distance
                A[row][col] = 2

    def dfs(self, A, island1, row, col):
        if A[row][col] == 2:
            return
        island1.append([row, col])
        A[row][col] = 2

        if row > 0 and A[row - 1][col] == 1:
            self.dfs(A, island1, row - 1, col)

        if col > 0 and A[row][col - 1] == 1:
            self.dfs(A, island1, row, col - 1)

        if row < len(A) - 1 and A[row + 1][col] == 1:
            self.dfs(A, island1, row + 1, col)

        if col < len(A[0]) - 1 and A[row][col + 1] == 1:
            self.dfs(A, island1, row, col + 1)


# if __name__ == "__main__":
#     s = Solution()
#     print(s.shortestBridge([[0, 1], [1, 0]]))
# @lc code=end
