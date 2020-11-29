#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        i = 0
        result = 0

        if length == 1:
            if flowerbed[0]:
                return n == 0
            return n <= 1

        while i < length:
            if flowerbed[i]:
                i += 2
                continue
            if i == 0 and not flowerbed[i + 1]:
                result += 1
                i += 2
                continue
            if not flowerbed[i - 1]:
                if i == length - 1:
                    result += 1
                    break
                if not flowerbed[i + 1]:
                    result += 1
                    i += 2
                    continue
            # here means front is flower
            i += 3
        return result >= n


# if __name__ == "__main__":
#     s = Solution()
#     print(s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
# @lc code=end
