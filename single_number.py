class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum([x*2 for x in set(nums)]) - sum(nums)