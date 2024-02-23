class Solution(object):
    def moveZeroes(self, nums):
        nums_length = len(nums)
        if nums_length <= 1:
            return

        bound = 0
        for i in range(1, nums_length):
            if nums[bound] != 0:
                bound += 1
            if nums[i] != 0:
                nums[bound], nums[i] = nums[i], nums[bound]
