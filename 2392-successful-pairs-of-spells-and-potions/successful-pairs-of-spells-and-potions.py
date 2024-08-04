class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        answer = list()
        for i in range(len(spells)):
            low, high = 0, len(potions) - 1
            while low <= high:
                mid = (low + high) // 2
                if spells[i] * potions[mid] >= success:
                    high = mid - 1
                else:
                    low = mid + 1
            if low == 0:
                answer.append(len(potions))
            elif high == len(potions) - 1:
                answer.append(0)
            else:
                answer.append(len(potions) - low)
        return answer