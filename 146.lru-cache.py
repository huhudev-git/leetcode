#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

class Node:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prve = None

    def _next(self, node: "Node"):
        self.next = node
        node.prve = self

    def _remove(self):
        self.prve._next(self.next)


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, 0)
        self.tail = Node(-1, 0)
        self.head._next(self.tail)
        self.capacity = capacity
        self.table = {}

    def _head(self, node):
        node._next(self.head.next)
        self.head._next(node)

    def get(self, key: int) -> int:
        node = self.table.get(key, None)
        if not node:
            return -1

        node._remove()
        self._head(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.table.get(key, None)

        if len(self.table) == self.capacity and not node:
            remove_node = self.tail.prve
            if remove_node.prve:
                remove_node._remove()
                del self.table[remove_node.key]

        if node:
            node.val = value
            node._remove()
        else:
            node = Node(key, value)
            self.table[key] = node

        self._head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
