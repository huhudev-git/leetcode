#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#

# @lc code=start
import heapq
from typing import List


class Solution:
    # def trapRainWater(self, heightMap: List[List[int]]) -> int:
    #     visit = [[0] * len(heightMap[0]) for _ in range(heightMap)]
    #     total = 0

    #     for row in range(1, len(heightMap)):
    #         for col in range(1, len(heightMap[0])-1):
    #             if visit[row][col] == 0:
    #                 self.dfs(heightMap, visit, row, col, total)

    # def dfs(self, heightMap, visit, row, col, total):
    #     level = heightMap[row][col]
    #     if visit[row][col]:
    #         return

    #     visit[row][col] = 1

    #     # ↑
    #     if heightMap[row - 1][col] < level:
    #         if row == 1:
    #             return 0
    #         self.dfs(heightMap, visit, row - 1, col)

    #     # ←
    #     if heightMap[row][col - 1] < level:
    #         if col == 1:
    #             return 0
    #         self.dfs(heightMap, visit, row, col - 1)

    #     # ↓
    #     if heightMap[row + 1][col] < level:
    #         if row == len(heightMap) - 2:
    #             return 0
    #         self.dfs(heightMap, visit, row + 1, col)

    #     # →
    #     if heightMap[row][col + 1] < level:
    #         if col == len(heightMap[0]) - 2:
    #             return 0
    #         self.dfs(heightMap, visit, row, col + 1)
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        row_num = len(heightMap)
        col_num = len(heightMap[0])
        if row_num < 3 or col_num < 3:
            return 0

        heap = []
        visit = [[False] * col_num for _ in range(row_num)]

        # put around block into heap
        for row in range(row_num):
            heapq.heappush(heap, (heightMap[row][0], row, 0))
            visit[row][0] = True
            heapq.heappush(heap, (heightMap[row][col_num-1], row, col_num-1))
            visit[row][col_num-1] = True

        for col in range(1, col_num-1):
            heapq.heappush(heap, (heightMap[0][col], 0, col))
            visit[0][col] = True
            heapq.heappush(heap, (heightMap[row_num-1][col], row_num-1, col))
            visit[row_num-1][col] = True

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        result = 0

        while heap:
            block = heapq.heappop(heap)
            height = block[0]
            row = block[1]
            col = block[2]

            # move ↑←↓→
            for d in range(4):
                x = row + dx[d]
                y = col + dy[d]

                # out of range
                if (x < 0 or x >= row_num) or (y < 0 or y >= col_num) or visit[x][y]:
                    continue

                # the (x, y) is lower than (row, col)
                if height > heightMap[x][y]:
                    # water in
                    result += height - heightMap[x][y]
                    # because water in, we raise the height
                    heightMap[x][y] = height

                heapq.heappush(heap, (heightMap[x][y], x, y))
                visit[x][y] = True

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.trapRainWater([
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]))

# @lc code=end
