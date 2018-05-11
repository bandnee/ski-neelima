# Enter your code here. Read input from STDIN. Print output to STDOUT

class Stack:
    def __init__(self):
        self.nums = []
        self.minelem = None

    def push(self, elem):
        if len(self.nums) == 0:
            self.nums.append(elem)
            self.minelem = elem
        elif (elem < self.minelem):
            top_replace = 2 * elem - self.minelem
            self.minelem = elem
            self.nums.append(top_replace)

    def pop(self):
        if len(self.nums) == 0:
            print("stack empty")
        else:
            top = self.nums.pop()
            if top < self.minelem:
                actual = self.minelem
                self.minelem = 2 * self.minelem - top
                return actual
            else:
                return top

    def getMin(self):
        return self.minelem


my_stk = Stack()
my_stk.push(8)
my_stk.push(4)
print(my_stk.getMin())
my_stk.pop()
print(my_stk.nums)
print(my_stk.getMin())