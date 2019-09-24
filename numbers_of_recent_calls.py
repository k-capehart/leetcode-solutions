class RecentCounter:
    times = []
    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        target = t - 3000
        self.times.append(t)
        while self.times[0] < target:
            self.times.pop(0)
        return len(self.times)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)