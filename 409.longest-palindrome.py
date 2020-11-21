#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = {i: 0 for i in s}
        for i in s:
            table[i] += 1

        result = 0
        flag = False
        for _, v in table.items():
            if v % 2 == 0:
                result += v
            else:
                result += (v - 1)
                flag = True
        if flag:
            return result + 1
        return result

    def longestPalindrome(self, s: str) -> int:
        table = [0 for i in range(128)]
        for i in s:
            table[ord(i)] += 1

        result = 0
        flag = False
        for i in table:
            if i % 2 == 0:
                result += i
            else:
                result += (i - 1)
                flag = True
        if flag:
            return result + 1
        return result
# @lc code=end
