class Solution:
    def compressedString(self, word: str) -> str:
        count = 0
        prev = None
        answer = ""
        for ch in word:
            if prev is None:
                prev = ch
                count += 1
            elif prev and ch == prev:
                count += 1
            else:
                for i in range(count // 9):
                    answer += f"9{prev}"
                if count % 9:
                    answer += f"{count % 9}{prev}"
                prev = ch
                count = 1
        for i in range(count // 9):
            answer += f"9{prev}"
        if count % 9:
            answer += f"{count % 9}{prev}"
        return answer

