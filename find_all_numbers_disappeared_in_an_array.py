class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        ls = set(range(1, nums_length+1))
        return ls-set(nums)