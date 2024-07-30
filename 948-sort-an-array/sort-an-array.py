class Solution:
    def mergeSort(self, left, mid, right, nums):
        elementInLeft = mid - left + 1
        elementInRight = right - mid
        
        leftElements = [0] * elementInLeft
        rightElements = [0] * elementInRight
    
        for i in range(elementInLeft):
            leftElements[i] = nums[left + i]
        for i in range(elementInRight):
            rightElements[i] = nums[mid + 1 + i]
        
        leftPointer = rightPointer = 0
        while leftPointer < elementInLeft and rightPointer < elementInRight:
            if leftElements[leftPointer] < rightElements[rightPointer]:
                nums[left] = leftElements[leftPointer]
                leftPointer += 1
            else:
                nums[left] = rightElements[rightPointer]
                rightPointer += 1
            left += 1
        
        while leftPointer < elementInLeft:
            nums[left] = leftElements[leftPointer]
            leftPointer += 1
            left += 1
        
        while rightPointer < elementInRight:
            nums[left] = rightElements[rightPointer]
            rightPointer += 1
            left += 1

    def merge(self, left, right, nums):
        if left < right:
            mid = (left + right) // 2
            self.merge(left, mid, nums)
            self.merge(mid + 1, right, nums)
            self.mergeSort(left, mid, right, nums)


    def sortArray(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        self.merge(left, right, nums)
        return nums