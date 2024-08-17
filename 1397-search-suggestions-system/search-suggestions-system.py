class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        answer = list()
        products.sort()
        left, right = 0, len(products) - 1
        for i in range(len(searchWord)):
            ch = searchWord[i]
            while left <= right and (len(products[left]) <= i or products[left][i] != ch):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != ch):
                right -= 1
            answer.append([])
            window_len = right - left + 1
            for j in range(min(window_len, 3)):
                answer[-1].append(products[left + j])
        return answer


