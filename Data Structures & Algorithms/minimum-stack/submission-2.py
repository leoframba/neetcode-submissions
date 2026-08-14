class MinStack:

    def __init__(self):
        self.min_s = []
        self.main_s = []

        

    def push(self, val: int) -> None:
        self.main_s.append(val)

        if not self.min_s or val < self.min_s[-1]:
            self.min_s.append(val)
        else:
            self.min_s.append(self.min_s[-1])

        

    def pop(self) -> None:
        self.min_s.pop()
        self.main_s.pop()

        

    def top(self) -> int:
#        self.min_s.pop()
        return self.main_s[-1]      

    def getMin(self) -> int:
        return self.min_s[-1]
        
