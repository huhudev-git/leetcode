#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

class TrieNode():

    def __init__(self):
        self.children = [None] * 128
        self.end = False

    def set_char(self, char):
        index = ord(char)
        node = TrieNode()
        self.children[index] = node
        return node

    def get_child(self, char):
        index = ord(char)
        return self.children[index]


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

    def search(self, root, word: str, index) -> bool:
        """
        Returns if the word is in the trie.
        """
        print(word[index:])
        if index == len(word):
            return root.end

        head = root
        for i in range(index, len(word)):
            w = word[i]
            if w == ".":
                for c in head.children:
                    if c and self.search(c, word, i+1):
                        return True
                return False
            else:
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


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.search(self.trie.root, word, 0)


if __name__ == "__main__":
    s = WordDictionary()
    s.addWord("bad")
    print(s.search("b.d"))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
