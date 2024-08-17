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

    def set_terminal(self):
        self.is_terminal = True
    
    def is_terminal_node(self):
        return self.is_terminal


class Trie:

    def __init__(self):
        self.node = Node()

    def insert(self, word: str) -> None:
        node_iter = self.node
        for ch in word:
            if not node_iter.char_exist(ch):
                node_iter.add_char(ch, Node())
            node_iter = node_iter.get_char_node(ch)
        node_iter.set_terminal()

    def search(self, word: str) -> bool:
        node_iter = self.node
        for ch in word:
            if not node_iter.char_exist(ch):
                return False
            node_iter = node_iter.get_char_node(ch)
        return node_iter.is_terminal_node()

    def startsWith(self, prefix: str) -> bool:
        node_iter = self.node
        for ch in prefix:
            if not node_iter.char_exist(ch):
                return False
            node_iter = node_iter.get_char_node(ch)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)