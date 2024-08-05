import heapq
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        char_to_count = dict()
        for ch in arr:
            char_to_count[ch] = char_to_count.get(ch, 0) + 1
        heap = list()
        for ch in arr:
            if char_to_count[ch] == 1:
                k -= 1
                if k == 0:
                    return ch
        return ""
