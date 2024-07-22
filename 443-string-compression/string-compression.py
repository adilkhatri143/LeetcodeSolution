class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        count = 0
        result = ""
        for i in range(len(chars)):
            if chars[i] == chars[j]:
                count += 1
            elif chars[i] != chars[j]:
                result += chars[j] + str(i - j) if (i - j) > 1 else chars[j]
                j = i
                count += 1
        result += chars[j] + str(i + 1 - j) if (i + 1 - j) > 1 else chars[j]
        for i in range(len(result)):
            chars[i] = result[i]
        return len(result)