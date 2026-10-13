#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#


# @lc code=start

from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        times = n / 3
        table = {}
        for i in nums:
            if i not in table:
                table[i] = 1
            else:
                table[i] += 1

        result = []
        for k, v in table.items():
            if v > times:
                result.append(k)

        return result

    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        return [x for x, c in Counter(nums).items() if c > n // 3]

    def majorityElement(self, nums: list[int]) -> list[int]:
        c1 = c2 = 0
        candidate1 = candidate2 = None

        for n in nums:
            if n == candidate1:
                c1 += 1
            elif n == candidate2:
                c2 += 1
            elif c1 == 0:
                candidate1, c1 = n, 1
            elif c2 == 0:
                candidate2, c2 = n, 1
            else:
                c1 -= 1
                c2 -= 1

        n = len(nums)
        return [c for c in (candidate1, candidate2)
                if c is not None and nums.count(c) > n // 3]

# @lc code=end
