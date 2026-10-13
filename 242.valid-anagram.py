#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = [0 for _ in range(26)]

        for c in s:
            n[ord(c) - ord('a')] += 1
        for c in t:
            n[ord(c) - ord('a')] -= 1

        return not any(n)
# @lc code=end
