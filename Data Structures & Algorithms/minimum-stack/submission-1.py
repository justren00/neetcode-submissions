class MinStack:

    def __init__(self):
        self.stack = []
        self.currMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.currMin and val > self.currMin[-1]:
            self.currMin.append(self.currMin[-1])
        else:
            self.currMin.append(val) 
        print(self.currMin)

    def pop(self) -> None:
        self.stack.pop()
        self.currMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currMin[-1]