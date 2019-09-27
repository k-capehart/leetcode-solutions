class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_len = len(stones)
        while stones_len > 1:
            stones.sort()
            x = stones[stones_len-1]
            y = stones[stones_len-2]
            if x == y:
                stones = stones[:stones_len-2:]
                stones_len -= 2
            elif x > y:
                stones[stones_len-2] = x-y
                stones = stones[:stones_len-1:]
                stones_len -= 1
            else:
                stones[stones_len-2] = y-x
                stones = stones[:stones_len-1:]
                stones_len -= 1
        if stones_len > 0:
            return stones[0]
        return 0