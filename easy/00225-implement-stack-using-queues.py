# https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x: int) -> None:
        while len(self.q2):
            self.q1.appendleft(self.q2.pop())
        self.q1.append(x)
    def pop(self) -> int:
        while len(self.q1):
            self.q2.appendleft(self.q1.pop())
        return self.q2.pop()
        
    def top(self) -> int:
        while len(self.q1):
            self.q2.appendleft(self.q1.pop())
        return self.q2[-1]
    def empty(self) -> bool:
        return not len(self.q1) and not len(self.q2)
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()