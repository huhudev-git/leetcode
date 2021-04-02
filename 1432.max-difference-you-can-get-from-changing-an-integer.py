#
# @lc app=leetcode id=1432 lang=python3
#
# [1432] Max Difference You Can Get From Changing an Integer
#

# @lc code=start
class Solution:
    def maxDiff(self, num: int) -> int:
        digits = self.get_digits(num)
        length = len(digits)
        max_digits = digits[:]
        min_digits = digits[:]

        for i in range(length):
            max_dig = max_digits[i]
            if max_dig != 9:
                max_digits = [9 if x == max_dig else x for x in max_digits]
                break

        if min_digits[0] != 1:
            min_dig = min_digits[0]
            min_digits = [1 if x == min_dig else x for x in min_digits]
        else:
            for i in range(1, length):
                min_dig = min_digits[i]
                if min_dig != 0 and min_dig != 1:
                    min_digits = [0 if x == min_dig else x for x in min_digits]
                    break

        _max = self.from_digits(max_digits)
        _min = self.from_digits(min_digits)
        return _max - _min

    def from_digits(self, arr):
        total = 0
        for i, v in enumerate(reversed(arr)):
            total += v * (10 ** i)
        return total

    def get_digits(self, n):
        result = []
        while n > 0:
            dig = n % 10
            result.insert(0, dig)
            n = n // 10
        return result
# @lc code=end
