class Node:
    def __init__(self):
        self.links = [None for i in range(26)]
        self.flag = False
    
    def contains_char(self, char):
        return self.links[ord(char) - 97]
    
    def set_char(self, char, new_node):
        self.links[ord(char) - 97] = new_node
    
    def get(self, char):
        return self.links[ord(char) - 97]
    
    def set_end(self):
        self.flag = True
    
    def is_end(self):
        return self.flag

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        itr_node = self.root
        for i in range(len(word)):
            if not itr_node.contains_char(word[i]):
                itr_node.set_char(word[i], Node())
            itr_node = itr_node.get(word[i])
        itr_node.set_end()

    def search(self, word: str) -> bool:
        itr_node = self.root
        for i in range(len(word)):
            if not itr_node.contains_char(word[i]):
                return False
            itr_node = itr_node.get(word[i])
        return itr_node.is_end()

    def startsWith(self, prefix: str) -> bool:
        itr_node = self.root
        for i in range(len(prefix)):
            if not itr_node.contains_char(prefix[i]):
                return False
            itr_node = itr_node.get(prefix[i])
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)