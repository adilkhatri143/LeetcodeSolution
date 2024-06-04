class Solution:
    def longestPalindrome(self, s: str) -> int:
        ht = dict()
        answer = 0
        contains_odd = False
        for ch in s:
            ht[ch] = ht.get(ch, 0) + 1
        
        for k, v in ht.items():
            if v % 2 == 0:
                answer += v
            if v % 2 == 1:
                answer += (v - 1)
                contains_odd = True
        return answer + 1 if contains_odd else answer