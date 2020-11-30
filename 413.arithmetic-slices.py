#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#

# @lc code=start
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        length = len(A)
        dp = [0 for _ in range(length)]

        for i in range(2, length):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = 1 + dp[i-1]
        return sum(dp)


# if __name__ == "__main__":
#     s = Solution()
#     s.numberOfArithmeticSlices([1, 2, 3, 8, 9, 10])

# @lc code=end
