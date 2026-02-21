class Trie:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.tag = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.children[ord(c) - ord('a')]:
                node.children[ord(c) - ord('a')] = self.TrieNode()
            node = node.children[ord(c) - ord('a')]
        node.tag = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not node.children[ord(c) - ord('a')]:
                return False
            node = node.children[ord(c) - ord('a')]
        return node.tag

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if not node.children[ord(c) - ord('a')]:
                return False
            node = node.children[ord(c) - ord('a')]
        return True
