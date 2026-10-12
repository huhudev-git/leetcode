#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

from collections import defaultdict

# @lc code=start

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        table = self.build_table(p)
        target_valid = len(table)
        window = defaultdict(int)
        result = []
        valid = 0
        l = 0

        for r, c in enumerate(s):
            window[c] += 1
            window_size = r - l + 1

            if window[c] == table[c]:
                valid += 1

            if window_size > len(p):
                if window[s[l]] == table[s[l]]:
                    valid -= 1
                window[s[l]] -= 1
                l += 1

            if window_size == len(p) and valid == target_valid:
                result.append(l)

        return result

    def build_table(self, p: str) -> dict[str, int]:
        table = defaultdict(int)
        for c in p:
            table[c] += 1
        return table
# @lc code=end
