class StreamChecker:
    def __init__(self, words: list[str]):
        self.trie = {}
        self.history = []
        self.max_len = 0
        for word in words:
            self.max_len = max(self.max_len, len(word))
            node = self.trie
            for char in reversed(word):
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = True

    def query(self, letter: str) -> bool:
        self.history.append(letter)
        node = self.trie
        for i in range(1, len(self.history) + 1):
            char = self.history[-i]
            if char not in node:
                return False
            node = node[char]
            if '#' in node:
                return True
        return False
