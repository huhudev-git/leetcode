#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    # 99.7% wtf?
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for s in strs:
            t = "".join(sorted(s))
            if t not in table:
                table[t] = [s]
            else:
                table[t].append(s)

        result = []
        for k in table:
            result.append(table[k])
        return result
# @lc code=end
