#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        length = len(nums)
        if length == 1:
            return nums[0]

        dp = [0 for _ in range(length)]
        dp[0] = nums[0]
        dp[1] = max(nums[0:2])

        for i in range(2, length):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[length - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.rob([5, 2, 6, 3, 1, 7]))

# @lc code=end
