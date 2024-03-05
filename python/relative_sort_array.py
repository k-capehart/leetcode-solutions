class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def customSort(x):
            return arr2.index(x)
        rem = []
        res = []
        for i in arr1:
            if i in arr2:
                res.append(i)
            else:
                rem.append(i)
        return sorted(res, key=customSort)+sorted(rem)