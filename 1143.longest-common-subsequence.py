#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

from functools import cache

# @lc code=start


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        return dfs(len(text1) - 1, len(text2) - 1)
# @lc code=end
