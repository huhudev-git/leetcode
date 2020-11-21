#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = [0 for _ in range(128)]
        reversed_table = {}

        index = 0
        last_index = index
        for p in pattern:
            n = ord(p)

            if table[n]:
                word = table[n]
                if table[n] == s[last_index: last_index + len(word)]:
                    if reversed_table[word] != n:
                        return False

                    index += (1 + len(word))
                    last_index = index
                    continue
                else:
                    return False
            else:
                while index < len(s) and s[index] != " ":
                    index += 1

                word = s[last_index: index]
                if reversed_table.get(word, 0):
                    return False

                table[n] = word
                reversed_table[word] = n

            index += 1
            last_index = index

        # if s not all matched
        return index == len(s) + 1

    def wordPattern(self, pattern: str, s: str) -> bool:
        reversed_table = {}
        table = {}

        words = s.split()
        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            p = pattern[i]
            word = words[i]

            if p not in table:
                if reversed_table.get(word, p) != p:
                    return False

                table[p] = word
                reversed_table[word] = p
            elif table[p] != word:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.wordPattern("abba", "dog cat cat dog"))

# @lc code=end
