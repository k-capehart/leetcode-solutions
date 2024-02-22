class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dist_to_target = {}
        indeces = {}
        nums_length = len(nums)
        for i in range(nums_length):
            num = nums[i]
            if(num in dist_to_target.keys() and num == (target - num)):
                return[indeces[num], i]
            dist_to_target[num] = target - num
            indeces[num] = i
        for i in nums:
            if(dist_to_target[i] in nums and indeces[i] != indeces[dist_to_target[i]]):
                return [indeces[i], indeces[dist_to_target[i]]]