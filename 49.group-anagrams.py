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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def build_tuple(str):
            c = [0] * 26
            for s in str:
                c[ord(s) - ord('a')] += 1
            return tuple(c)

        table = {}
        for str in strs:
            t = build_tuple(str)
            if t not in table:
                table[t] = []
            table[t].append(str)
        return list(table.values())
# @lc code=end
