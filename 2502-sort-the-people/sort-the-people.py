class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            heights[i] = (heights[i], names[i])
        heights.sort(key=lambda x: -x[0])
        return [name for height, name in heights]