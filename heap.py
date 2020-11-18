class Heap:
    def __init__(self):
        self.size = 0
        self.items = []

    def getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1
    def getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2
    def getParentIndex(self, childIndex):
        return (childIndex-1)//2
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    def hasParent(self,index):
        return self.getParentIndex(index) >= 0
    def leftChild(self, index):
        return self.items[self.getLeftChildIndex(index)]
    def rightChild(self, index):
        return self.items[self.getRightChildIndex(index)]
    def parent(self, index):
        return self.items[self.getParentIndex(index)]

    def swap(self, a, b):
        self.items[a], self.items[b] = self.items[b], self.items[a]

