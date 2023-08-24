class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.validWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.validWord = True

    def isValidWord(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.validWord

    def remove(self, word):
        def removeHelper(node, word, depth):
            if depth == len(word):
                node.validWord = False
                return node.children.count(None) == len(node.children)

            index = ord(word[depth]) - ord('a')
            if not node.children[index]:
                return False

            shouldRemove = removeHelper(node.children[index], word, depth + 1)

            if shouldRemove:
                node.children[index] = None
                return node.children.count(None) == len(node.children)
            return False

        removeHelper(self.root, word, 0)
