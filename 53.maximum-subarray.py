#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0 for _ in range(length)]

        result = nums[0]
        dp[0] = nums[0]
        for i in range(1, length):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            if result < dp[i]:
                result = dp[i]
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([1, 2]))

# @lc code=end
