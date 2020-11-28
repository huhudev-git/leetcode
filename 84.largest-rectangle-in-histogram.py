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
        # 定义遍历heights数组的下标值
        i = 0
        # 定义heights数组元素构成的面积最大值
        max_value = 0
        # 定义栈来保存单增序列
        stack = []
        # 此处较为巧妙。若heights数组中元素都是单增序列，则最后无法出栈stack，也就无法计算最大面积，所以补个0，使之最后可以出栈
        heights.append(0)
        while i < length:
            print(stack)
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                now_idx = stack.pop()
                if len(stack) == 0:
                    max_value = max(max_value, i * heights[now_idx])
                else:
                    print(i - stack[-1] - 1, heights[now_idx])
                    max_value = max(max_value, (i - stack[-1] - 1) * heights[now_idx])

        return max_value


if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([1, 2, 3, 4, 5]))
# @lc code=end
