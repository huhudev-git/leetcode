#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []

        for interval in intervals:
            if not result or result[-1][-1] < interval[0]:
                result.append(interval)
            else:
                result[-1][-1] = max(interval[-1], result[-1][-1])
        return result


# @lc code=end
