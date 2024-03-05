class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sum_num = sum([x for x in A if x % 2 == 0])
        for query in queries:
            prev = A[query[1]]
            A[query[1]] = A[query[1]] + query[0]
            if A[query[1]] % 2 == 0 and prev % 2 == 0:
                sum_num = (sum_num - prev) + A[query[1]]
            elif A[query[1]] % 2 == 0:
                sum_num+=A[query[1]]
            elif prev % 2 == 0:
                sum_num-=prev
            ans.append(sum_num)
        return ans