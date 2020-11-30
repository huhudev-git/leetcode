#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from collections import deque


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        result = [[0 for _ in range(n)] for _ in range(m)]

        q = deque()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append([[i, j], 0])

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        visited = [[0 for _ in range(n)] for _ in range(m)]

        while q:
            tmp, distance = q.popleft()
            x, y = tmp[0], tmp[1]

            if matrix[x][y] == 1:
                result[x][y] = distance

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] != 1:
                    q.append([[nx, ny], distance + 1])
                    visited[nx][ny] = 1
        return result

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    top = matrix[i - 1][j] + 1 if i > 0 else 10E10
                    left = matrix[i][j - 1] + 1 if j > 0 else 10E10
                    matrix[i][j] = min(top, left)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                bottom = matrix[i + 1][j] + 1 if i < m - 1 else 10E10
                right = matrix[i][j + 1] + 1 if j < n - 1 else 10E10
                matrix[i][j] = min(matrix[i][j], bottom, right)

        return matrix

# @lc code=end
