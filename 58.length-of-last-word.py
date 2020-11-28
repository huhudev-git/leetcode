#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        find_word = False
        word_end_len = length
        for i in range(length - 1, -1, -1):
            if s[i] == " ":
                if find_word:
                    return word_end_len - i
            else:
                if not find_word:
                    find_word = True
                    word_end_len = i

        if find_word:
            return word_end_len + 1
        return 0

    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        index = length - 1
        while index >= 0 and s[index] == " ":
            index -= 1

        if index < 0:
            return 0

        result = 0
        while index >= 0 and s[index] != " ":
            index -= 1
            result += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("a"))
# @lc code=end
