#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        end = intervals[0][-1]
        start = intervals[0][0]
        result = []

        for interval in intervals[1:]:
            if interval[0] <= end:
                if interval[-1] > end:
                    end = interval[-1]
            else:
                result.append([start, end])
                start = interval[0]
                end = interval[-1]

        if not result or result[-1][-1] < start:
            result.append([start, end])

        return result

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []

        for interval in intervals:
            if not result or result[-1][-1] < interval[0]:
                result.append(interval)
            else:
                result[-1][-1] = max(interval[-1], result[-1][-1])
        return result


# if __name__ == "__main__":
#     s = Solution()
#     print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))

# @lc code=end
