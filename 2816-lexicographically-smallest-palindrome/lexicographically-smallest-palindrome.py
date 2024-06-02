class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        char = list(s)
        left, right = 0, len(char) - 1
        while left < right:
            if ord(char[left]) < ord(char[right]):
                char[right] = char[left]
            else:
                char[left] = char[right]
            left += 1
            right -= 1
        return "".join(char)
