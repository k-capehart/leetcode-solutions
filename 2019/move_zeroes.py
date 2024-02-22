class Solution:
    def moveZeroes(self, nums: List[int]) -> None:  
        total_0s = 0
        for num in nums:
            if num == 0:
                total_0s += 1
        
        for i in range(total_0s):
            nums.remove(0)
            nums.append(0)