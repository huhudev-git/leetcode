#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_ = 0
        table = [0 for i in range(128)]

        index = 0
        length = len(s)

        while index < length:
            c = s[index]
            n = ord(c)
            if table[n] != 0:
                if max_ < index - start:
                    max_ = index - start

                start = table[n]
                index = table[n]
                table = [0 for i in range(128)]
            else:
                index += 1
                table[n] += index

        if max_ < index - start:
            return index - start
        return max_

    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        table = [0 for i in range(128)]
        begin = 0
        word = ""
        length = len(s)

        for i in range(length):
            n = ord(s[i])

            table[n] += 1
            # if not appeared
            if table[n] == 1:
                # current length
                word += s[i]
                if result < len(word):
                    result = len(word)
            else:
                # move to 1
                while begin < i and table[n] > 1:
                    table[ord(s[begin])] -= 1
                    begin += 1

                word = s[begin: i+1]
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("dvdf"))

# @lc code=end
