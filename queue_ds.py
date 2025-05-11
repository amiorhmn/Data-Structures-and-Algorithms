class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __repr__(self):
        nodes = []
        curr: Node = self.head
        while curr is not None:
            nodes.append(curr.value)
            curr = curr.next
        return ", ".join(nodes)
    
    def __len__(self) -> int:
        curr: Node = self.head
        i = 0
        while curr is not None:
            i = i + 1
            curr = curr.next
        return i


    def enqueue(self, value):
        node = Node(value, None)
        if self.head is None: # if empty
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        

    def dequeue(self):
        if self.head is None: # if empty
            return None

        temp = self.head
        self.head = self.head.next
        if self.head.next is None:
            self.tail = None
        return temp.value



# Time complexity:
#----------------
# enqueue O(1)
# dequeue O(1)