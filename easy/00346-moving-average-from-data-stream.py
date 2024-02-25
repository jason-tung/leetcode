# https://leetcode.com/problems/moving-average-from-data-stream/
class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.tot = 0
    def next(self, val: int) -> float:
        if len(self.queue) >= self.size:
            self.tot -= self.queue.pop()
        self.queue.appendleft(val)
        self.tot += val
        return self.tot / len(self.queue)
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)