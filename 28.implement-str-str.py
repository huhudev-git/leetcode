#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or not needle:
            return 0

        length = len(haystack)
        nlength = len(needle)
        for i in range(length - nlength + 1):
            if haystack[i] == needle[0]:
                ok = True
                for j in range(1, nlength):
                    if haystack[i + j] != needle[j]:
                        ok = False
                        break
                if ok:
                    return i

        if haystack == needle:
            return 0
        return -1


# if __name__ == "__main__":
#     s = Solution()
#     s.strStr("abc", "c")
# @lc code=end
