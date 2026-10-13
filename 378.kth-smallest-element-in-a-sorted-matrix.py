#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 把每一行看成一条有序链表，问题就变成“合并 n 个有序链表，取第 k 个”（同 23 题）
        # 堆里存 (值, 行, 列)，堆顶永远是当前所有候选里最小的
        n = len(matrix)
        heap = [(matrix[i][0], i, 0) for i in range(min(n, k))]  # 超过 k 行的部分用不到
        heapq.heapify(heap)

        # 弹出 k-1 个最小值，每弹出一个，就把它同一行的下一个元素补进堆
        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))

        # 此时堆顶就是第 k 小
        return heap[0][0]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r = matrix[0][0], matrix[-1][-1]

        while l < r:
            mid = l + (r - l) // 2
            c = self.count(matrix, mid)
            if c >= k:
                r = mid
            else:
                l = mid + 1

        return l

    def count(self, matrix: List[List[int]], target: int) -> int:
        i, j = len(matrix) - 1, 0
        count = 0

        while i >= 0 and j < len(matrix):
            if matrix[i][j] <= target:
                count += i + 1
                j += 1
            else:
                i -= 1

        return count
# @lc code=end
