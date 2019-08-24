class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self,data):
        self.size += 1
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.previous = None
            self.tail.next = None
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            self.tail.next = None

    def prepend(self,data):
        new_node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = self.tail = new_node
            self.head.previous = None
            self.tail.next = None
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            self.head.previous = None

    def display(self):
        current = self.head;
        if self.head is None:
            return
        while current != None:
            print(current.data,end = '->');
            current = current.next;
        print(current)

dList = DoublyLinkedList();
dList.append(1);
dList.append(2);
dList.append(3);
dList.append(4);
dList.append(5);
dList.prepend(6)
dList.display();