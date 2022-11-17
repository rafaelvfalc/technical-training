class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data=data)
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = new_node

    def length(self):
        current_node = self.head
        total = 0

        while current_node.next != None:
            total += 1
            current_node = current_node.next

        return total

    def display(self):
        elems = []
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)

        print(elems)

    def get(self, index):
        current_index = 0
        current_node = self.head

        try:
            while True:
                current_node = current_node.next
                if(current_index == index):
                    return current_node.data
                current_index += 1
        except AttributeError:
            print("ERROR: Index out of range!")
            return

    def erase(self, index):
        current_index = 0
        current_node = self.head

        try:
            while True:
              last_node = current_node
              current_node = current_node.next
              if(current_index == index):
                  last_node.next = current_node.next
                  return
              current_index += 1
        except AttributeError:
            print("ERROR: Index out of range!")
            return  


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.display()
    my_list.append(0)
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.display()
    print("Index #2: ", my_list.get(2))
    my_list.erase(1)
    my_list.display()
    print("Index #2: ", my_list.get(2))
