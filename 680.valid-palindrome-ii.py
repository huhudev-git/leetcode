#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self._validPalindrome(s, 0)

    def _validPalindrome(self, s: str, count) -> bool:
        start = 0
        end = len(s) - 1

        while start <= end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue

            start_lower = s[start].lower()
            end_lower = s[end].lower()

            if start_lower != end_lower:
                if count:
                    return False

                case1 = False
                case2 = False
                if s[start+1].lower() == end_lower:
                    case1 = self._validPalindrome(s[start + 1: end + 1], count+1)
                if start_lower == s[end-1].lower():
                    case2 = self._validPalindrome(s[start: end], count+1)
                return case1 or case2

            end -= 1
            start += 1
        return True


# if __name__ == "__main__":
#     s = Solution()
#     print(s.validPalindrome("aqbca"))
# @lc code=end
