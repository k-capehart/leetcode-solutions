# Zeller's Rule
# f = k + [(13*m-1)/5] + D + [D/4] + [C/4] - 2*C.
        
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days_of_week = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
        k = day
        m = ((month-3)%12) + 1
        D = int(str(year)[2::])
        if month < 3:
            D-=1
        C = int(str(year)[:2:])
        f = k + (((13*m)-1)//5) + D + (D//4) + (C//4) - (2*C)
        return days_of_week[f%7]