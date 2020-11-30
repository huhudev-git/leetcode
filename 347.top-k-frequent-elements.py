#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1

        s = sorted(counter.items(), key=lambda x: (x[1], x[0]), reverse=True)
        return [s[i][0] for i in range(k)]


# if __name__ == "__main__":
#     s = Solution()
#     s.topKFrequent([1, 1, 1, 1, 2, 2, 3], 2)
# @lc code=end
