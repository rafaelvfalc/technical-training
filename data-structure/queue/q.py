class Queue(object):
    
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        try:
            self.items.pop(0)
        except IndexError:
            print("Queue is empty!")

    def peek(self):
        try:
            return self.items[0]
        except IndexError:
            print("Queue is empty!")

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def print_queue(self):
        print(self.items)

if __name__ == '__main__':
    queue = Queue()

    print(queue.is_empty())
    queue.peek()
    queue.pop()
    queue.push(1)
    queue.print_queue()
    print(queue.size())
    print(queue.is_empty())
    queue.push(2)
    queue.print_queue()
    print(queue.size())
    print(queue.is_empty())
    queue.pop()
    queue.print_queue()
    print(queue.size())
    print(queue.is_empty())
    queue.pop()
    queue.print_queue()
    print(queue.size())
    print(queue.is_empty())
