#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[-1])
        index = 0
        count = 0
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= intervals[index][-1]:
                index = i
                continue
            else:
                count += 1
        return count

# @lc code=end
