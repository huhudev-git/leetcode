#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp = nums
        temp = list(set(temp))

        # record num times > 1
        table = {}
        for i in nums:
            if i not in table:
                table[i] = 0
            table[i] += 1

        # generate with unique nums
        res = [[]]
        for index in range(len(temp)):
            for j in range(len(res)):
                # copy list
                curr = list(res[j])
                curr.append(temp[index])
                res.append(curr)

        # print(res)
        # print(table)

        # for each num > 2
        # for the list include the num which in res
        # we add remain times
        # 重复的数字唯一可能性的组合就是在原基础之上继续加一个他自己
        for k, v in table.items():
            if v <= 1:
                continue

            # only select list which has k
            old_group = []
            for r in res:
                if k in r:
                    old_group.append(r)

            v -= 1
            while v > 0:
                # select from old group
                length = len(old_group)
                # new list put in new group
                new_group = []
                for l in range(length):
                    curr = list(old_group[l])
                    curr.append(k)
                    new_group.append(curr)

                # print(new_group)
                res.extend(new_group)
                # we need this turn group for next turn
                old_group = new_group
                v -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1, 1, 2, 2]))
# @lc code=end
