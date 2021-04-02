#
# @lc app=leetcode id=1598 lang=python3
#
# [1598] Crawler Log Folder
#

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log == "./":
                continue
            if log == "../":
                if count > 0:
                    count -= 1
                continue
            count += 1
        return count

# @lc code=end
