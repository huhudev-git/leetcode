#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3:
            return 0

        heap = []
        result = 0
        visit = [False for _ in range(length)]

        heapq.heappush(heap, (height[0], 0))
        visit[0] = True
        heapq.heappush(heap, (height[length - 1],  length - 1))
        visit[-1] = True

        while heap:
            x = heapq.heappop(heap)
            index = x[1]
            h = height[index]

            for x in [-1, 1]:
                x = index + x
                if (x < 0 or x >= length) or visit[x]:
                    continue

                if h > height[x]:
                    result += h - height[x]
                    height[x] = h

                heapq.heappush(heap, (height[x], x))
                visit[x] = True
        return result

    def trap(self, height: List[int]) -> int:
        pre_max = [height[0]]
        post_max = [height[-1]]
        length = len(height)

        for i in range(1, length):
            pre_h = height[i]
            post_h = height[length - i - 1]

            pre_max.append(max(pre_h, pre_max[-1]))
            post_max.append(max(post_h, post_max[-1]))

        post_max = list(reversed(post_max))
        result = 0

        for i in range(length):
            h = min(pre_max[i], post_max[i])
            result += (h - height[i])

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# @lc code=end
