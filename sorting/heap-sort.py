from abc import abstractmethod, ABC

class HeapNode():
    def __init__(self, number: float):
        self.number = number
        self.left: HeapNode | None = None
        self.right: HeapNode | None = None


class Heap():
    def __init__(self):
        self.root: HeapNode | None = None

    def add_node(self, node_to_add: HeapNode):
        self.__add_node(node_to_add, self.root)

    def __add_node(self, node_to_add: HeapNode, parent_node: HeapNode):
        if node_to_add.number > parent_node.number:
            if parent_node.left is None:
                parent_node.left = node_to_add
            elif parent_node.right is None:
                parent_node.right = node_to_add


h2 = HeapNode(2)
h5 = HeapNode(5)
h7 = HeapNode(7)
h13 = HeapNode(13)
h25 = HeapNode(25)

heap = Heap()
heap.add_node(h2)
heap.add_node(h5)
heap.add_node(h7)
heap.add_node(h13)
heap.add_node(h25)