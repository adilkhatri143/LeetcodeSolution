class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_set = set()
        num_to_count = Counter(arr)
        for k, v in num_to_count.items():
            if v in unique_set:
                return False
            unique_set.add(v)
        return True
