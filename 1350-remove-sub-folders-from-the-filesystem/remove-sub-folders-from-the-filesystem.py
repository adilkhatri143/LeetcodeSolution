class TreeNode():
    def __init__(self):
        self.childs = dict()
        self.is_terminal = False
    

class Trie:
    def __init__(self):
        self.node = TreeNode()
    
    def insert(self, word):
        itr = self.node
        words = word.split("/")
        for ch in words:
            if ch not in itr.childs:
                itr.childs[ch] = TreeNode()
            itr = itr.childs[ch]
        itr.is_terminal = True
    
    def search(self, word):
        itr = self.node
        words = word.split("/")
        for i in range(len(words)):
            if itr.childs[words[i]].is_terminal and i != len(words) - 1:
                return False
            itr = itr.childs.get(words[i])
        return True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        result = list()
        for f in folder:
            trie.insert(f)
        for f in folder:
            if trie.search(f):
                result.append(f)
        return result

