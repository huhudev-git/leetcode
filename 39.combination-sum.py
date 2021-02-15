#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(filter(lambda x: x <= target, candidates))
        candidates.sort()

        result = []
        item = []

        self.gen(candidates, item, 0, target, result)
        return result

    def gen(self, candidates, item, index, target, result):
        if target == 0:
            result.append(item[:])
            return

        for i in range(index, len(candidates)):
            candidate = candidates[i]
            if candidate > target:
                return

            item.append(candidate)
            self.gen(candidates, item, i, target - candidate, result)
            item.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))

# @lc code=end
