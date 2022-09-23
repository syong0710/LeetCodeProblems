class MyQue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    # add an element at the end of the queue
    def push(self, x:int) -> None:
        self.stack_in.append(x)

    # check if the queue is empty
    def ifEmpty(self):
        return not(self.stack_in or self.stack_out)

    # return and remove the element at the head of the queue
    def pop(self) ->int:
        if self.ifEmpty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    # get the front element
    def peek(self) -> int:
        value = self.pop()
        self.stack_out.append(value)
        return value

myQue1 = MyQue()
myQue1.push(1)
myQue1.push(3)
myQue1.push(5)
print(myQue1.peek())
print(myQue1.pop())
print(myQue1.peek())
print(myQue1.ifEmpty())







