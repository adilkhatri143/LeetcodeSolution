class Solution:
    global_list = list()
    def solve(self, nums, visited, temp):
        if len(nums) == len(temp):
            self.global_list.append(temp)
            return
        
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
                self.solve(nums, visited, temp + [nums[i]])
                visited.remove(nums[i])
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.global_list = list()
        visited = set()
        self.solve(nums, visited, [])
        return self.global_list