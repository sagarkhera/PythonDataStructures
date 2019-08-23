class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    #O(1)
    def prepend(self,data):
        self.size += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    #O(1)
    def getsize(self):
        return self.size

    #O(n)
    def traverse(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data,end='->')
            cur_node = cur_node.next
        print(cur_node)

    #O(n)
    def append(self,data):
        self.size += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node

    #O(n)
    def remove(self,data):
        cur_node = self.head
        prev_node = None
        self.size -= 1
        if self.head is None:
            return
        while cur_node is not None and cur_node.data != data:
            prev_node = cur_node
            cur_node = cur_node.next
        if prev_node is None:
            self.head = cur_node.next
        elif cur_node is not None:
            prev_node.next = cur_node.next

myList = LinkedList()
myList.prepend(4)
myList.prepend(2)
myList.prepend(1)
myList.prepend(8)
myList.append(5)
myList.append(9)
myList.remove(1)
myList.traverse()
print(myList.getsize())

# Output
# 8->2->4->5->9->None
# 5