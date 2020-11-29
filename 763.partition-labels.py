#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        positions = {}
        for i, s in enumerate(S):
            if s not in positions:
                positions[s] = [i, i]
            else:
                positions[s][-1] = i

        result = []
        end = 0
        last_end = end
        for i, s in enumerate(S):
            if positions[s][-1] > end:
                end = positions[s][-1]

            # if reach end, update position
            if i == end:
                result.append(end - last_end + 1)
                last_end = end + 1

        return result


# if __name__ == "__main__":
#     s = Solution()
#     print(s.partitionLabels("vhaagbqkaq"))

# @lc code=end
