class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_set = set(dictionary)
        answer = list()
        for word in sentence.split(" "):
            temp = ""
            for ch in word:
                temp += ch
                if temp in word_set:
                    break
            answer.append(temp)
        return " ".join(answer)
            