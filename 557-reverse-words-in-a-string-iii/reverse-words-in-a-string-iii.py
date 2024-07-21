class Solution:
    def reverseWords(self, s: str) -> str:
        i = j = 0
        decode_str = []
        while i < len(s):
            if s[i] == " ":
                pass
            else:
                j = i
                while j < len(s) and s[j] != " ":
                    j += 1
                temp_ptr = j - 1
                while temp_ptr >= i:
                    decode_str.append(s[temp_ptr])
                    temp_ptr -= 1
                decode_str.append(" ")
                i = j
            i += 1
        decode_str[-1] = ""
        return "".join(decode_str)
