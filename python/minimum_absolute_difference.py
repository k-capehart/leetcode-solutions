class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        abs_diff = 100000
        res = []
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff < abs_diff:
                abs_diff = diff
                res = [[arr[i], arr[i+1]]]
            elif diff == abs_diff:
                res.append([arr[i], arr[i+1]])
        return res