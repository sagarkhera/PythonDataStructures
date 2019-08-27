class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def append(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data,self.root)    

    def insertNode(self,data,node):
        if data < node.data:
            if node.leftChild:
                return self.insertNode(data,node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                return self.insertNode(data,node.rightChild)
            else:
                node.rightChild = Node(data)

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self,node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
    
    def getMax(self,node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data
    
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)
            
    def traverseInOrder(self,node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        
        print("%s " % node.data)
        
        if node.rightChild:
            self.traverseInOrder(node.rightChild)
            
bst = BinarySearchTree()
bst.append(12)
bst.append(13)
bst.append(21)
bst.append(31)
bst.append(11)
bst.append(11)

bst.traverse()
print()
print(bst.getMaxValue())
print(bst.getMinValue())




