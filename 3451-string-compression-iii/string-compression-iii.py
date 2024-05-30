class Solution:
    def compressedString(self, word: str) -> str:
        st = list()
        count = 0
        for ch in word:
            if st and st[-1][0] == ch:
                top_data = st.pop()
                st.append((top_data[0], top_data[1] + 1))
            else:
                st.append((ch, 1))
        answer = ""
        while st:
            ch, count = st.pop()
            time = count // 9
            if count % 9:
                answer = f"{count % 9}{ch}" + answer
            for i in range(time):
                answer = f"9{ch}" + answer
        return answer

