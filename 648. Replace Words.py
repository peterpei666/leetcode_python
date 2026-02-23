from typing import List

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.tag = False

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = self.TrieNode()
        for word in dictionary:
            node = root
            for c in word:
                index = ord(c) - ord('a')
                if node.children[index] is None:
                    node.children[index] = self.TrieNode()
                node = node.children[index]
            node.tag = True
        words = sentence.split()
        for i in range(len(words)):
            node = root
            for j in range(len(words[i])):
                if node.tag:
                    words[i] = words[i][:j]
                    break
                if node.children[ord(words[i][j]) - ord('a')]:
                    node = node.children[ord(words[i][j]) - ord('a')]
                else:
                    break
        return ' '.join(words)
