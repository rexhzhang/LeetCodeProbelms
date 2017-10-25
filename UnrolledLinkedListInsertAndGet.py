class Node():
    '''This '''

    def __init__(self):
        self.arr = []
        self.next = None


class UnrolledLinkedList():
    def __init__(self, max_node_capacity=16):
        self.max_node_capacity = max_node_capacity
        self.length = 0
        self.head = None
        self.tail = None

    def __getitem__(self, index):
        if index > self.length - 1 or index < 0:  # Over the max
            raise IndexError(str(index) + ' out of range.')

        currentNode = self.head
        currentIndex = 0
        # Iterate until the right node is found.
        while len(currentNode.arr) - 1 + currentIndex < index:
            currentIndex = currentIndex + len(currentNode.arr)
            currentNode = currentNode.next

        # We have the right node, time to get the item from the array.
        arrIndex = index - currentIndex
        return currentNode.arr[arrIndex]  # Delete the data at the final index
