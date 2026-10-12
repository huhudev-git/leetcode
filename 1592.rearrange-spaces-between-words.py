#
# @lc app=leetcode id=1592 lang=python3
#
# [1592] Rearrange Spaces Between Words
#

# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        count_spaces = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return words[0] + ' ' * count_spaces

        spaces_between_words = count_spaces // (len(words) - 1)
        extra_spaces = count_spaces % (len(words) - 1)
        return (' ' * spaces_between_words).join(words) + ' ' * extra_spaces

    def reorderSpaces(self, text: str) -> str:
        count_spaces = 0
        words = []
        current_word = ''

        for char in text:
            if char == ' ':
                count_spaces += 1
                if current_word:
                    words.append(current_word)
                    current_word = ''
            else:
                current_word += char

        if current_word:
            words.append(current_word)

        if len(words) == 1:
            return words[0] + ' ' * count_spaces

        spaces_between_words = count_spaces // (len(words) - 1)
        extra_spaces = count_spaces % (len(words) - 1)
        return (' ' * spaces_between_words).join(words) + ' ' * extra_spaces


# @lc code=end
