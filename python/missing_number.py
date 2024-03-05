class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) - (sum(nums) - sum(range(len(nums))))