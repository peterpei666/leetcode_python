from typing import List

class MagicDictionary:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.tag = False

    def __init__(self):
        self.root = self.TrieNode()

    def buildDict(self, dictionary):
        for word in dictionary:
            node = self.root
            for c in word:
                index = ord(c) - ord('a')
                if node.children[index] is None:
                    node.children[index] = self.TrieNode()
                node = node.children[index]
            node.tag = True

    def search(self, word):
        return self.dfs(self.root, word, 0, False)

    def dfs(self, node, word, idx, change):
        if node is None:
            return False
        if idx == len(word):
            return node.tag and change
        if change:
            return self.dfs(node.children[ord(word[idx]) - ord('a')], word, idx + 1, True)
        else:
            ans = self.dfs(node.children[ord(word[idx]) - ord('a')], word, idx + 1, False)
            for i in range(26):
                if i != ord(word[idx]) - ord('a') and not ans:
                    ans = ans or self.dfs(node.children[i], word, idx + 1, True)
            return ans
