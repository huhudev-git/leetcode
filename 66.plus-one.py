#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        digits[length - 1] += 1

        for i in range(length - 1, 0, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i - 1] += 1

        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits

# @lc code=end
