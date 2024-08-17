class TreeNode:
    def __init__(self):
        self.alphabet = [False] * 26
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.node = TreeNode()

    def insert(self, word: str) -> None:
        node_iter = self.node
        for ch in word:
            if not node_iter.alphabet[ord(ch) - 97]:
                node_iter.alphabet[ord(ch) - 97] = TreeNode()
            node_iter = node_iter.alphabet[ord(ch) - 97]
        node_iter.is_terminal = True

    def search(self, word: str) -> bool:
        node_iter = self.node
        for ch in word:
            if not node_iter.alphabet[ord(ch) - 97] or not node_iter.alphabet[ord(ch) - 97].is_terminal:
                return float("-inf")
            node_iter = node_iter.alphabet[ord(ch) - 97]
        return len(word)

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        words.sort()
        max_len = float("-inf")
        answer = ""
        for word in words:
            if trie.search(word) > max_len:
                max_len = len(word)
                answer = word
        return answer

        