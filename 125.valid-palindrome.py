#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start <= end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue

            if s[start].lower() == s[end].lower():
                end -= 1
                start += 1
            else:
                return False
        return True


# if __name__ == "__main__":
#     s = Solution()
#     s.isPalindrome("A man, a plan, a canal: Panama")

# @lc code=end
