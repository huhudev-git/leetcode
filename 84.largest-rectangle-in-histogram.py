#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        递增栈
        """
        length = len(heights) + 1
        i = 0
        max_value = 0
        stack = []
        heights.append(0)

        while i < length:
            if not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                now_idx = stack.pop()
                if stack:
                    max_value = max(max_value, (i - stack[-1] - 1) * heights[now_idx])
                else:
                    max_value = max(max_value, i * heights[now_idx])
        return max_value


# if __name__ == "__main__":
#     s = Solution()
#     print(s.largestRectangleArea([1, 2, 3, 4, 5]))
# @lc code=end
