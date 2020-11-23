#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
from typing import List


class DisjointSet:
    def __init__(self, n):
        # Constructor to create and
        # initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        self.count = n

    # Finds set of given item x

    def find(self, x):
        # Finds the representative of the set
        # that x is an element of
        if (self.parent[x] != x):

            # if x is not the parent of itself
            # Then x is not the representative of
            # its set,
            self.parent[x] = self.find(self.parent[x])

            # so we recursively call Find on its parent
            # and move i's node directly under the
            # representative of this set

        return self.parent[x]

    # Do union of two sets represented
    # by x and y.
    def union(self, x, y):
        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)

        # If they are already in same set
        if xset == yset:
            return

        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        # If ranks are same, then move y under
        # x (doesn't matter which one goes where)
        # and increment rank of x's tree
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1

        self.count -= 1


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        s = DisjointSet(len(M))
        for i in range(len(M)):
            for j in range(i):
                if M[i][j]:
                    s.union(i, j)

        return s.count


# if __name__ == "__main__":
#     s = Solution()
#     print(s.findCircleNum([
#         [1, 0, 0, 1],
#         [0, 1, 1, 0],
#         [0, 1, 1, 1],
#         [1, 0, 1, 1]
#     ]))

# @lc code=end
