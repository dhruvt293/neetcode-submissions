class MinStack:

    def __init__(self):
        self.ns = []
        self.ms = []
    
        

    def push(self, val: int) -> None:
        self.ns.append(val)
        if not self.ms or val <= self.ms[-1]:
            self.ms.append(val)

        

    def pop(self) -> None:
        if self.ns[-1] == self.ms[-1]:
            self.ms.pop()
        self.ns.pop()
        

    def top(self) -> int:
        return self.ns[-1]
        

    def getMin(self) -> int:
        return self.ms[-1]
        
