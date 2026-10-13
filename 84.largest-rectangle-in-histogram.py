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

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        result = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                index = stack.pop()
                left = stack[-1] if stack else -1  # 左边第一根比它矮的柱子的下标
                result = max(result, (i - left - 1) * heights[index])
            stack.append(i)  # 比 i 高的柱子要先全部弹出去，i 才能放进栈
        return result

# if __name__ == "__main__":
#     s = Solution()
#     print(s.largestRectangleArea([1, 2, 3, 4, 5]))
# @lc code=end
