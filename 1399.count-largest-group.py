#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#

# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        table = [0 for i in range(37)]
        for i in range(1, n + 1):
            total = self.sum_of_digits(i)
            table[total] += 1
        _max = max(table)
        count = table.count(_max)
        return count

    def sum_of_digits(self, n):
        total = 0
        while n > 0:
            dig = n % 10
            total = total + dig
            n = n // 10
        return total
# @lc code=end
