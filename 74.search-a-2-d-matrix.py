#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])
        if not n:
            return False

        start = 0
        end = m - 1

        while start < end:
            mid = (start + end) // 2
            if matrix[mid][0] > target:
                end = mid - 1
            elif matrix[mid][0] < target:
                start = mid + 1
            else:
                return True

        if matrix[start][0] > target:
            start -= 1
        arr = matrix[start]

        start = 0
        end = n - 1

        while start < end:
            mid = (start + end) // 2
            if arr[mid] > target:
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                return True

        return arr[start] == target


# if __name__ == "__main__":
#     s = Solution()
#     print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11))
    # print(s.searchMatrix([[1]], 1))

# @lc code=end
