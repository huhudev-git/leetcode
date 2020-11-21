#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        table = {}
        length = len(s)
        for i in range(length-9):
            word = s[i:i+10]
            if word in table:
                table[word] += 1
            else:
                table[word] = 1

        result = []
        for k, v in table.items():
            if v > 1:
                result.append(k)
        return result


if __name__ == "__main__":
    s = Solution()
    s.findRepeatedDnaSequences("AAAAAAAAAAA")
# @lc code=end
