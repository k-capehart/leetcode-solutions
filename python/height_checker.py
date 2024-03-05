class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0
        for x,y in zip(sorted_heights, heights):
            if x != y:
                count+=1
        return count
    