#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        length = len(temperatures)
        result = [0 for _ in range(length)]
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, index = stack.pop()
                result[index] = i - index
            stack.append((t, i))
        return result
# @lc code=end
