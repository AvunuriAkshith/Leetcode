class MinStack:

    def __init__(self):
        self.arr = []
        self.minarr = []

    def push(self, value: int) -> None:
        self.arr.append(value)

        if not self.minarr or value <= self.minarr[-1]:
            self.minarr.append(value) 

    def pop(self) -> None:
        if self.arr.pop() == self.minarr[-1]:
            return self.minarr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minarr[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()