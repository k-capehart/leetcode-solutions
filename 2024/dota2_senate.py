class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_list = []
        d_list = []

        while "D" in senate and "R" in senate:
            new_senate = ""
            for senator in senate:
                if (senator == 'D'):
                    if (r_list):
                        r_list.pop()
                    else:
                        d_list.append(1)
                        new_senate += 'D'
                if (senator == 'R'):
                    if (d_list):
                        d_list.pop()
                    else:
                        r_list.append(1)
                        new_senate += 'R'
            senate = new_senate

        return "Radiant" if 'R' in senate else "Dire"
