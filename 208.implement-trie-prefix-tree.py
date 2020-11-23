#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start

class TrieNode():

    def __init__(self):
        self._children = [None] * 128
        self.end = False

    def set_char(self, char):
        index = ord(char)
        node = TrieNode()
        self._children[index] = node
        return node

    def get_child(self, char):
        index = ord(char)
        return self._children[index]


class Trie:
    """
    noob implement
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        head = self.root
        for w in word:
            node = head.get_child(w)
            if node:
                head = node
            else:
                head = head.set_char(w)
        head.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        head = self.root
        for w in word:
            node = head.get_child(w)
            if node:
                head = node
            else:
                return False
        return head.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        head = self.root
        for w in prefix:
            node = head.get_child(w)
            if node:
                head = node
            else:
                return False
        return True


# if __name__ == "__main__":
#     t = Trie()
#     t.insert("Trie")
#     print(t.search("Trie"))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
