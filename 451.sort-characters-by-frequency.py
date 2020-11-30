#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        for i in s:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1

        s = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        result = ""
        for k, v in s:
            result = f"{result}{k * v}"
        return result


# if __name__ == "__main__":
#     s = Solution()
#     s.frequencySort("tree")
# @lc code=end
