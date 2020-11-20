#
# @lc app=leetcode id=871 lang=python3
#
# [871] Minimum Number of Refueling Stops
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def minRefuelStops(
        self,
        target: int,
        startFuel: int,
        stations: List[List[int]],
    ) -> int:
        if startFuel >= target:
            return 0
        if not stations and startFuel < target:
            return -1

        stations.append([target, 0])
        stations = sorted(stations, key=lambda x: x[0])
        gas_list = []
        times = 0

        for station in stations:
            # next station distance
            distance = station[0]

            # if we have gas station
            # if we need add gas
            while gas_list and startFuel < distance:
                # change past -> we add gas in previous
                startFuel -= heapq.heappop(gas_list)
                times += 1

            # if even we add gas the startFuel isn't enough
            if (not gas_list) and startFuel < distance:
                return -1

            # we may add gas later
            heapq.heappush(gas_list, -station[1])
        return times


if __name__ == "__main__":
    s = Solution()
    print(s.minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]))
# @lc code=end
