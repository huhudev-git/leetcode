#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return 0

        result = 0
        mx = max(nums)
        mi = min(nums)
        bucket_length = max(1, (mx - mi) // (length - 1))
        buckets = [[] for _ in range((mx - mi) // bucket_length + 1)]

        for num in nums:
            i = (num - mi) // bucket_length
            buckets[i].append(num)

        last = float('inf')
        for i in range(len(buckets)):
            if buckets[i]:
                if last != float('inf'):
                    result = max(result, min(buckets[i]) - last)
                last = max(buckets[i])

        return result
# @lc code=end
