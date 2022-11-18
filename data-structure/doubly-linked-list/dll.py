class Node:

    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node
    
    def get_prev(self):
        return self.previous
    
    def set_prev(self, new_node):
        self.previous = new_node

    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data

class DoublyLinkedList:

    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        if not self.root:
            self.root = Node(data)
            self.size += 1
            return
        else:
            this_node = self.root
            while(this_node):
                if(this_node.get_next()):
                    this_node = this_node.get_next()
                else:
                    this_node.set_next(Node(data, None, this_node))
                    self.size += 1
                    return

    def remove(self, data):
        this_node = self.root

        while(this_node):
            if(this_node.get_data() == data):
                next = this_node.get_next()
                prev = this_node.get_prev()

                if(next):
                    next.set_prev(prev)
                if(prev):
                    prev.set_next(next)
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                this_node = this_node.get_next()
        return False

    def find(self, data):
        this_node = self.root
        while(this_node):
            if(this_node.get_data() == data):
                return this_node
            else:
                this_node = this_node.get_next()
        return None

    def display(self):
        elems = []
        this_node = self.root

        while(this_node):
            elems.append(this_node.get_data())
            this_node = this_node.next

        print(elems)

if __name__ == '__main__':
    my_list = DoublyLinkedList()
    print(my_list.get_size())
    my_list.display()
    my_list.add(0)
    print(my_list.get_size())
    my_list.display()
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
    my_list.add(4)
    my_list.display()
    print(my_list.get_size())
    my_list.remove(3)
    my_list.display()
    print(my_list.get_size())
    my_list.remove(2)
    my_list.display()
    print(my_list.get_size())
