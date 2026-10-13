#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c = 0
        candidate = -1

        for n in nums:
            if c == 0:
                candidate = n
                c += 1
                continue

            c += 1 if n == candidate else -1

        return candidate

# @lc code=end
