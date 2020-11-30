#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points = sorted(points, key=lambda x: x[0])

        people = 1
        end = points[0][-1]

        for point in points:
            #   ---
            # -----
            if point[0] <= end:
                # ----
                # -----
                # 需要更新区间终点
                if point[-1] < end:
                    end = point[-1]
            # 起点都比之前重点大，就加一个人
            else:
                people += 1
                end = point[-1]

        return people


if __name__ == "__main__":
    s = Solution()
    s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])

# @lc code=end
