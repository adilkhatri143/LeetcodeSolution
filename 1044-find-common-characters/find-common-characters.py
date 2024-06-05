class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count_char = [0] * 26
        for i in range(len(words[0])):
            count_char[ord(words[0][i]) - 97] += 1
        for i in range(len(words)):
            count_char_next = [0] * 26
            for j in range(len(words[i])):
                count_char_next[ord(words[i][j]) - 97] += 1
            for k in range(26):
                count_char[k] = min(count_char[k], count_char_next[k])
        
        answer = list()
        for i in range(26):
            while count_char[i]:
                answer.append(chr(i + 97))
                count_char[i] -= 1
        return answer
        


            