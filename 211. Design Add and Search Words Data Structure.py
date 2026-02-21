class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.tag = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.children[ord(c) - ord('a')]:
                node.children[ord(c) - ord('a')] = self.TrieNode()
            node = node.children[ord(c) - ord('a')]
        node.tag = True

    def search(self, word: str) -> bool:
        def find(node, idx):
            if idx == len(word):
                return node.tag
            if word[idx] == '.':
                ans = False
                for i in range(26):
                    if node.children[i]:
                        ans = find(node.children[i], idx + 1)
                    if ans:
                        break
                return ans
            if node.children[ord(word[idx]) - ord('a')]:
                return find(node.children[ord(word[idx]) - ord('a')], idx + 1)
            return False
        
        return find(self.root, 0)
