class TreeNode():
    def __init__(self):
        self.childs = dict()
        self.is_terminal = False
    

class Trie:
    def __init__(self):
        self.node = TreeNode()
    
    def insert(self, word):
        itr = self.node
        words = word.split("/")[1:]
        for ch in words:
            if ch not in itr.childs:
                itr.childs[ch] = TreeNode()
            itr = itr.childs[ch]
        itr.is_terminal = True
    
    def search(self, word):
        itr = self.node
        words = word.split("/")[1:]
        temp_str = ""
        for ch in words:
            if ch in itr.childs and itr.childs[ch].is_terminal:
                temp_str += ch
                return temp_str
            temp_str += ch
            itr = itr.childs.get(ch)
        return temp_str

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        exist = set()
        trie = Trie()
        result = list()
        for f in folder:
            trie.insert(f)
        folder.sort(key=lambda x: len(x))
        for f in folder:
            temp_str = trie.search(f)
            if temp_str not in exist:
                exist.add(temp_str)
                result.append(f)
        return result

