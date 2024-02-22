class Solution(object):
    def moveZeroes(self, nums):
        x = 0
        y = len(nums)
        while x < y:
            if nums[x] == 0:
                nums.pop(x)
                nums.append(0)
                y = y - 1
            else:
                x = x + 1
