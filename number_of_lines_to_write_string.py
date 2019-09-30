import math
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        width_map = dict(zip("abcdefghijklmnopqrstuvwxyz", widths))
        s_values = [width_map[x] for x in S ]
        sum_x = 0
        last_x = 0
        lines = 1
        for x in s_values:
            last_x = x
            if sum_x+x > 100:
                sum_x = 0
                lines+=1
            sum_x+=x
        return [lines, sum_x]