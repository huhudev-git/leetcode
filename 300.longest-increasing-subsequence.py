#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0 for _ in range(length)]

        result = 1
        dp[0] = 1
        for i in range(1, length):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1

            if result < dp[i]:
                result = dp[i]

        return result

    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        stack = [nums[0]]
        for i in range(1, len(nums)):
            if stack[-1] < nums[i]:
                stack.append(nums[i])
            else:
                # here can use bin search (sorted list)
                for j in range(len(stack)):
                    if stack[j] >= nums[i]:
                        stack[j] = nums[i]
                        break
        return len(stack)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))

# @lc code=end
