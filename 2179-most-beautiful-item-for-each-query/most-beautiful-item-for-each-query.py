class Solution:
    def binary_search(self, query, items):
        max_beauty = 0
        low, high = 0, len(items) - 1
        while low <= high:
            mid = (low + high) // 2
            if items[mid][0] <= query:
                low = mid + 1
                max_beauty = max(max_beauty, items[mid][1])
            else:
                high = mid - 1
        return max_beauty
    
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        maximum = float("-inf")
        for idx, item in enumerate(items):
            items[idx][1] = max(maximum, items[idx][1])
            maximum = items[idx][1]
        ans = list()
        for query in queries:
            ans.append(self.binary_search(query, items))
        return ans