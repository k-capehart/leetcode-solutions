class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_count = 0
        d_count = 0

        while "D" in senate and "R" in senate:
            new_senate = ""
            for senator in senate:
                if (senator == 'D'):
                    if (r_count):
                        r_count -= 1
                    else:
                        d_count += 1
                        new_senate += 'D'
                if (senator == 'R'):
                    if (d_count):
                        d_count -= 1
                    else:
                        r_count += 1
                        new_senate += 'R'
            senate = new_senate

        return "Radiant" if 'R' in senate else "Dire"
