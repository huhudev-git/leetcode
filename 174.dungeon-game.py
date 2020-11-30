#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#

# @lc code=start
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        \
         \
          \
        ↑ up -> down is wrong
        """
        # 到达i,j至少需要多少初始血量
        dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

        # 到达i,j的血量
        life_map = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

        if dungeon[0][0] <= 0:
            dp[0][0] = -dungeon[0][0] + 1
            life_map[0][0] = 1
        else:
            dp[0][0] = 1
            life_map[0][0] = dungeon[0][0] + 1

        for j in range(1, len(dungeon[0])):
            if dungeon[0][j] >= 0:
                # here hero life must > 0
                life_map[0][j] = life_map[0][j-1] + dungeon[0][j]
                dp[0][j] = dp[0][j-1]
            else:
                life_map[0][j] = life_map[0][j-1] + dungeon[0][j]
                if life_map[0][j] <= 0:
                    dp[0][j] = dp[0][j-1] - life_map[0][j] + 1
                    life_map[0][j] = 1
                else:
                    dp[0][j] = dp[0][j-1]

        for i in range(1, len(dungeon)):
            if dungeon[i][0] >= 0:
                life_map[i][0] = life_map[i-1][0] + dungeon[i][0]
                dp[i][0] = dp[i-1][0]
            else:
                life_map[i][0] = life_map[i-1][0] + dungeon[i][0]
                if life_map[i][0] <= 0:
                    dp[i][0] = dp[i-1][0] - life_map[i][0] + 1
                    life_map[i][0] = 1
                else:
                    dp[i][0] = dp[i-1][0]

        for i in range(1, len(dungeon)):
            for j in range(1, len(dungeon[0])):

                if dungeon[i][j] >= 0:
                    #   9
                    # 5 x
                    if dp[i-1][j] > dp[i][j-1]:
                        life_map[i][j] = life_map[i][j-1] + dungeon[i][j]
                        dp[i][j] = dp[i][j-1]
                    else:
                        life_map[i][j] = life_map[i-1][j] + dungeon[i][j]
                        dp[i][j] = dp[i-1][j]
                else:
                    left_in_life = life_map[i][j-1] + dungeon[i][j]
                    if left_in_life <= 0:
                        left_in_dp = dp[i][j-1] - left_in_life + 1
                    else:
                        left_in_dp = dp[i][j-1]

                    up_in_life = life_map[i-1][j] + dungeon[i][j]
                    if up_in_life <= 0:
                        up_in_dp = dp[i-1][j] - up_in_life + 1
                    else:
                        up_in_dp = dp[i-1][j]

                    if up_in_dp > left_in_dp:
                        dp[i][j] = left_in_dp
                        if left_in_life <= 0:
                            life_map[i][j] = 1
                        else:
                            life_map[i][j] = left_in_life
                    else:
                        dp[i][j] = up_in_dp
                        if up_in_life <= 0:
                            life_map[i][j] = 1
                        else:
                            life_map[i][j] = up_in_life

        for i in life_map:
            print(i)
        print('------')
        for i in dp:
            print(i)

        return dp[-1][-1]

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # 从i,j到终点至少需要多少血量
        dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

        # 到达i,j的血量
        life_map = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

        if dungeon[-1][-1] <= 0:
            dp[-1][-1] = -dungeon[-1][-1] + 1
        else:
            dp[-1][-1] = 1

        for j in range(len(dungeon[0])-2, -1, -1):
            dp[-1][j] = max(1 - dungeon[-1][j+1], 1)

        for i in range(len(dungeon)-2, -1, -1):
            dp[i][-1] = max(dp[i+1][-1] - dungeon[i][-1], 1)

        for i in range(len(dungeon)-2, -1, -1):
            for j in range(len(dungeon[0])-2, -1, -1):
                # 从下方或者左边进来
                # 选需要血量最小的
                min_life = min(dp[i+1][j], dp[i][j+1])
                # 看当前最少需要多少
                dp[i][j] = max(min_life - dungeon[i][j], 1)

        return dp[0][0]


# if __name__ == "__main__":
#     s = Solution()
#     # s.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
#     s.calculateMinimumHP([
#         [1, -3, 3],
#         [0, -2, 0],
#         [-3, -3, -3]
#     ])

# @lc code=end
