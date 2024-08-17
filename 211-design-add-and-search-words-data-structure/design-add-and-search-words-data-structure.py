class Node:
    def __init__(self):
        self.alphabet = [False] * 26
        self.is_terminal = False
    
    def char_exist(self, ch):
        return self.alphabet[ord(ch) - 97]

    def add_char(self, ch, new_node):
        self.alphabet[ord(ch) - 97] = new_node
    
    def get_char_node(self, ch):
        return self.alphabet[ord(ch) - 97]
    
    def get_char_by_idx(self, idx):
        return self.alphabet[idx]

    def set_terminal(self):
        self.is_terminal = True
    
    def is_terminal_node(self):
        return self.is_terminal

class WordDictionary:

    def __init__(self):
        self.node = Node()

    def addWord(self, word: str) -> None:
        node_iter = self.node
        for ch in word:
            if not node_iter.char_exist(ch):
                node_iter.add_char(ch, Node())
            node_iter = node_iter.get_char_node(ch)
        node_iter.set_terminal()

    def search(self, word: str) -> bool:
        def dfs(idx, word, node_iter):
            if idx == len(word):
                return node_iter.is_terminal_node()
            if word[idx] == ".":
                for i in range(26):
                    if node_iter.alphabet[i] != False and dfs(idx + 1, word, node_iter.get_char_by_idx(i)):
                        return True
            else:
                new_char = node_iter.get_char_node(word[idx])
                if new_char != False:
                    return dfs(idx + 1, word, new_char)
            return False
        node_iter = self.node
        return dfs(0, word, node_iter)        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)