class StackOverflowError(Exception):
    pass


class StackUnderflowError(Exception):
    pass


class MyStack:

    def __init__(self, capacity):
        self._data = []
        self._capacity = capacity

    def is_empty(self):
        return len(self._data) == 0

    def is_full(self):
        return len(self._data) == self._capacity

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError("Stack is empty")
        return self._data.pop()

    def push(self, value):
        if self.is_full():
            raise StackOverflowError("Stack is full")
        self._data.append(value)

    def top(self):
        if self.is_empty():
            raise StackUnderflowError("Stack is empty")
        return self._data[-1]


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)

print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
