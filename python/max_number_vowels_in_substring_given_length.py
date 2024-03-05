class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        str_len = len(s)

        if str_len == k:
            return k

        vowels = ['a', 'e', 'i', 'o', 'u']
        values = []
        sum = 0
        max_sum = 0

        for i in range(str_len):
            if s[i] in vowels:
                values.append(1)
            else:
                values.append(0)
            if i >= k:
                sum -= values[i-k]
            sum += values[i]
            if sum == k:
                return k
            if sum > max_sum:
                max_sum = sum

        return max_sum
