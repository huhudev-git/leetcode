#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from typing import List
import queue


class Solution:
    # too slow
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.insert(0, beginWord)
        if endWord not in wordList:
            wordList.append(endWord)
            target = len(wordList)
        else:
            target = wordList.index(endWord)

        length = len(wordList)
        graph = [[] for _ in range(length)]
        visit = [False for _ in range(length)]

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

        return self.bfs(graph, 0, target, visit)

    def bfs(self, graph, start, target, visit):
        q = queue.Queue()
        q.put((start, 1))

        while not q.empty():
            node = q.get()
            if node[0] == target:
                return node[1]

            for c in graph[node[0]]:
                if not visit[c]:
                    q.put((c, node[1] + 1))
                    visit[c] = True
        return 0


if __name__ == "__main__":
    s = Solution()
    # print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    # print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

# @lc code=end
