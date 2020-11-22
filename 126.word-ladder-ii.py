#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
import queue
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if beginWord not in wordList:
            wordList.insert(0, beginWord)
            start = 0
        else:
            start = wordList.index(beginWord)

        if endWord not in wordList:
            wordList.append(endWord)
            target = len(wordList)
        else:
            target = wordList.index(endWord)

        length = len(wordList)
        graph = [[] for _ in range(length)]

        for i in range(length):
            for j in range(i + 1, length):
                word = wordList[i]
                compare_word = wordList[j]

                not_same = 0
                for k in range(len(word)):
                    if word[k] != compare_word[k]:
                        not_same += 1
                        if not_same > 1:
                            break

                if not_same == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        parent, back = self.bfs(graph, start, target)
        print(parent, back)

        result = []
        for i in back:
            path = [endWord]
            node = i
            while node != -1:
                path.append(wordList[node])
                node = parent[node]
            result.append(list(reversed(path)))
        return result

    def bfs(self, graph, start, target):
        visit = [0 for _ in graph]
        parent = [-1 for _ in graph]

        q = queue.Queue()

        # (node distance parent)
        q.put((start, 1, -1))
        min_path_num = 0
        visit[start] = 1
        # target parents
        result = []
        time = 0

        # below wrong
        # TODO
        while not q.empty():
            node = q.get()

            if min_path_num != 0 and node[1] > min_path_num:
                break

            if node[0] == target:
                min_path_num = node[1]
                result.append(time)

            for c in graph[node[0]]:
                if (visit[c] == 0) or (visit[c] == node[1] + 1):
                    parent[c] = time
                    q.put((c, node[1] + 1, time))
                    visit[c] = node[1] + 1
            time += 1
        return parent, result


if __name__ == "__main__":
    s = Solution()
    # print(s.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    # print(s.findLadders("a", "c", ["a", "b", "c"]))
    print(s.findLadders("red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]))

# @lc code=end
