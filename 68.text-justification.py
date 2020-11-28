#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        self.fill_line(words, 0, maxWidth, result)

        # process last line
        last_line = result[-1]
        line = ""
        per_is_word = True
        for i in last_line:
            if i == " ":
                if per_is_word:
                    line += i
                    per_is_word = False
            else:
                per_is_word = True
                line += i

        space_num = maxWidth - len(line)
        line += " " * space_num
        result[-1] = line
        return result

    def fill_line(self, words, start, maxWidth, result):
        if start == len(words):
            return

        end = start
        total = 0
        word_total = 0

        # use word start - end(end not include)
        while end < len(words):
            total += len(words[end]) + 1
            word_total += len(words[end])

            # print(words[end], total)
            if total - 1 == maxWidth:
                end += 1
                break
            elif total > maxWidth:
                total -= len(words[end]) + 1
                word_total -= len(words[end])
                break
            end += 1

        # print(start, end)
        # 单词个数
        word_num = end - start
        # print(word_num)
        # 空格数量
        space_num = maxWidth - word_total
        # print(space_num, maxWidth, word_total)
        # 每个词至少多少空格
        if word_num != 1:
            per_space = space_num // (word_num - 1)
        else:
            per_space = 0
        # print(per_space)
        # 多出几个空格
        last_space = space_num - per_space * (word_num - 1)
        # print(last_space)

        line = ""
        if per_space:
            for i in range(start, end - 1):
                word = words[i]
                line = f"{line}{word}{' ' * per_space}"
                if last_space:
                    line = f"{line} "
                    last_space -= 1
            line = f"{line}{words[end-1]}"
        else:
            line = f'{words[end - 1]}{" " *last_space }'

        result.append(line)
        self.fill_line(words, end, maxWidth, result)


if __name__ == "__main__":
    s = Solution()
    # s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16)
    """
    "This    is    an"
    "This is an examp"
    """
# @lc code=end
