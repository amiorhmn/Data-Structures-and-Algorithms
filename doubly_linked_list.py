#######################################################
## Has both head and tail pointer, but no dummy head ##
#######################################################

class Node:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedList:
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



    def get_value(self, index):
        i = 0
        curr: Node = self.head
        while i < index and curr is not None:
            i = i + 1
            curr = curr.next

        # If the while loop was broken because curr is None, then raise index error
        if curr is None:
            raise IndexError(f"Index {index} does not exist")
        
        return curr.value
    


    def set_value(self, index, value):
        i = 0
        curr: Node = self.head
        while i < index and curr is not None:
            i = i + 1
            curr = curr.next

        # If the while loop was broken because curr is None, then raise index error
        if curr is None:
            raise IndexError(f"Index {index} does not exist")
        
        curr.value = value



    def append(self, value):
        node = Node(value)
        if self.head is None: # check if empty
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    

    def prepend(self, value):
        node = Node(value)
        if self.head is None: # check if empty
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            

    
    def insert(self, index, value):
        if index == 0:  # if insertion at the start
            self.prepend(value)
        else:
            i = 0
            curr = self.head
            while i < index and curr is not None:   # loop until reaching index or the end
                i = i + 1
                curr = curr.next
            if curr is None:    # reached the end
                if i == index:  # reached index
                    self.append(value)
                else:   # reached the end but not index
                    raise IndexError(f"Cannot insert at index {index}")
            else:
                node = Node(value, curr.prev, curr)
                curr.prev.next = node
                curr.prev = node



    def pop(self):
        popped = self.tail

        if popped is None:   # Handle empty list
            raise IndexError("Cannot pop from empty list")
        
        if self.head.next is None:  # If one node in the list
            self.head = None
            self.tail = None
        else:   # more than one node in the list
            self.tail = self.tail.prev
            self.tail.next = None

        return popped.value
    


    def shift(self):
        shifted = self.head

        if shifted is None:   # Handle empty list
            raise IndexError("Cannot shift from empty list")
        
        if self.head.next is None:  # If one node in the list
            self.head = None
            self.tail = None
        else:   # more than one node in the list
            self.head = self.head.next
            self.head.prev = None

        shifted.next = None     # remove dangling reference
        return shifted.value
    


    def remove(self, index):
        if index == 0:  # if removal at the start
            return self.shift()    # alternate: self.pop()
        else:
            i = 0
            curr = self.head
            while i < index and curr is not None:   # loop until reaching index or the end
                i = i + 1
                curr = curr.next

            if curr is None:    # reached the end
                raise IndexError(f"Index {index} does not exist")
            
            if curr.next is None: #last node is at index
                return self.pop()
            
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.prev = None
            curr.next = None

            return curr.value
        


    def reverse(self):
        curr = self.head

        if curr is None:    # if empty list, then return self
            return self 
        
        while curr is not None:     # starting from head untill the end for each node swap its next and prev properties
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp

            curr = temp     # go to next node

        # swap the head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

        return self


# Time complexity:
# ---------------
# get_value   O(n)
# set_value   O(n)
# append      O(1)
# prepend     O(1)
# insert      O(n)
# pop         O(1)
# shift       O(1)
# remove      O(n)
# reverse     O(n)