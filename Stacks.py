class Stack:
    def __init__(self,n):
        self.n = n
        self.stack = [] #When you want something to be an empty list, place []
    
    def push(self,a):
        if len(self.stack) < self.n:
            self.stack.append(a)
        else:
            print("The stack is full. If you wish to add a new element, please first take one out.")

    def pop(self):
        if len(self.stack) == 0:
            print("The stack is empty. If you wish to take away an element, please first put one in.")
        else:
            self.stack.pop(-1) #0 is the first number, -1 is the last; it's called negative indexing.
    
    def printlast(self):
        if len(self.stack) == 0:
            print("There are no elements in this stack.")
        else:
            print(self.stack[-1])

    def stackamount(self):
        if len(self.stack) == 0:
            print("There are no elements in this stack.")
        else:
            print("The number of elements in this stack is", len(self.stack))

    def printstack(self):
        if len(self.stack) == 0:
            print("There are no elements in this stack.")
        else:
            print("The elements in the stack are", self.stack)

stack=Stack(5)

stack.push(4)
stack.push(56)
stack.push(874)
stack.push(23)
stack.push(86)

stack.printstack()

stack.push(1)

stack.pop()
stack.pop()
stack.pop()

stack.printstack()

stack.pop()
stack.pop()
stack.pop()

stack.push(54)
stack.push(24)
stack.push(74)
stack.push(73)
stack.push(83)

stack.printlast()

stack.stackamount()