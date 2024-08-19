class TrieNode:
    def __init__(self):
        self.childs = dict()
        self.word = None
        self.is_terminal = False
    

class Trie:
    def __init__(self):
        self.node = TrieNode()
    
    def insert(self, word):
        itr = self.node
        for ch in word:
            if ch not in itr.childs:
                itr.childs[ch] = TrieNode()
            itr = itr.childs[ch]
        itr.is_terminal = True
        itr.word = word
    
    def search(self, board, row, col, itr, final_ans):
        if itr.is_terminal:
            itr.is_terminal = False
            final_ans.append(itr.word)
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for x, y in direction:
            new_row = row + x
            new_col = col + y
            if 0 <= new_row <= len(board) - 1 and 0 <= new_col <= len(board[0]) - 1 and board[new_row][new_col] != "" and board[new_row][new_col] in itr.childs:
                original_val = board[row][col]
                board[row][col] = ""
                self.search(board, new_row, new_col, itr.childs.get(board[new_row][new_col]), final_ans)
                board[row][col] = original_val

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        answer = list()
        trie = Trie()
        for word in words:
            trie.insert(word)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie.node.childs:
                    trie.search(board, row, col, trie.node.childs.get(board[row][col]), answer)
        return answer

[
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]]