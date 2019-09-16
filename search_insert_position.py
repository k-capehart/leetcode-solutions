class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        hig = len(nums) - 1
        mid = int(hig/2)
        
        if target < nums[0]: return 0
        if target > nums[hig]: return hig+1
        
        while hig - low > 1:
            if(target == nums[mid]):
                return mid
            elif(target < nums[mid]):
                hig = mid
                mid = int((low + hig)/2)
            elif(target > nums[mid]):
                low = mid
                mid = int((low + hig)/2)
                
        if(nums[low] == target): return low
        return hig