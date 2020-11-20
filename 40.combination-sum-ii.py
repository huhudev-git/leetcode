#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(filter(lambda x: x <= target, candidates))
        if sum(candidates) < target:
            return []

        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for i in range(1, target + 1):
            for j in range(len(candidates)):
                if candidates[j] > i:
                    break

                for k in range(len(dp[i - candidates[j]])):
                    temp = dp[i - candidates[j]][k][:]
                    # check if this number is used
                    if len(temp) > 0 and temp[-1] >= j:
                        continue

                    # store index
                    temp.append(j)
                    dp[i].append(temp)
        res = []
        check = {}
        for temp in dp[target]:
            value = [candidates[t] for t in temp]
            key = str(value)
            if key in check:
                check[key] += 1
            else:
                check[key] = 1
                res.append(value)
        return res

    # ===========================
    # too slow
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(filter(lambda x: x <= target, candidates))
        if sum(candidates) < target:
            return []

        result = []
        item = []
        self.gen(candidates, item, 0, target, 0, result)
        return list(map(lambda x: list(x), result))

    def gen(self, candidates, item, index, target, sum_, result):
        if index >= len(candidates) or sum_ > target:
            return

        sum_ += candidates[index]
        item.append(candidates[index])
        if sum_ == target:
            t = tuple(sorted(item))
            if t not in result:
                result.append(t)

        self.gen(candidates, item, index + 1, target, sum_, result)

        sum_ -= candidates[index]
        item.pop()
        self.gen(candidates, item, index + 1, target, sum_, result)


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

# @lc code=end
