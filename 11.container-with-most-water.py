#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0

        while l < r:
            hl, hr = height[l], height[r]
            if hl > hr:
                area = max((r - l) * hr, area)
                while l < r and height[r] <= hr:  # 跳过
                    r -= 1
            else:
                area = max((r - l) * hl, area)
                while l < r and height[l] <= hl:  # 跳过
                    l += 1

        return area

# @lc code=end
