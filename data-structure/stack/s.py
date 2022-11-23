class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            print("Stack is empty!")

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty!")

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def print_stack(self):
        print(self.items)

if __name__ == '__main__':
    stack = Stack()

    print(stack.is_empty())
    stack.peek()
    stack.pop()
    stack.push(1)
    stack.print_stack()
    print(stack.size())
    print(stack.is_empty())
    stack.push(2)
    stack.print_stack()
    print(stack.size())
    print(stack.is_empty())
    stack.pop()
    stack.print_stack()
    print(stack.size())
    print(stack.is_empty())
    stack.pop()
    stack.print_stack()
    print(stack.size())
    print(stack.is_empty())
