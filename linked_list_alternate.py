#####################################
## Has tail pointer and dummy head ##
#####################################

# Implemented using a dummy head node instead of a head pointer which makes prepending easier
# Implemented using a tail pointer which makes appending and poping O(1) instead of O(n)

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        node = Node(value=None)
        self.head = node  # head.value will always remain empty and head.next will point to the actual first element
        self.tail = node

    def __repr__(self):
        nodes = []
        curr: Node = self.head.next
        while curr is not None:
            nodes.append(curr.value)
            curr = curr.next
        return ", ".join(nodes)
    
    def __len__(self) -> int:
        curr: Node = self.head.next
        i = 0
        while curr is not None:
            i = i + 1
            curr = curr.next
        return i



    def get_value(self, index):
        i = 0
        curr: Node = self.head.next
        while i < index and curr is not None:
            i = i + 1
            curr = curr.next

        # If the while loop was broken because curr is None, then raise index error
        if curr is None:
            raise IndexError(f"Index {index} does not exist")
        
        return curr.value


    
    def set_value(self, index, value):
        i = 0
        curr: Node = self.head.next
        while i < index and curr is not None:
            i = i + 1
            curr = curr.next

        # If the while loop was broken because curr is None, then raise index error
        if curr is None:
            raise IndexError(f"Index {index} does not exist")
        
        curr.value = value
    


    def append(self, value):
        node = Node(value, None)
        self.tail.next = node
        self.tail = node



    def prepend(self, value):
        node = Node(value, self.head.next)
        self.head.next = node



    def insert(self, index, value):
        # if insert at the start
        if index == 0:
            self.prepend(value)
        else:
            i = 0
            curr: Node = self.head.next
            while i < index - 1 and curr is not None:
                i = i + 1
                curr = curr.next

            # If the while loop was broken because curr is None, then raise index error
            if curr is None:
                raise IndexError(f"Cannot insert at index {index}")
            # if insert at the end
            elif curr.next is None:
                self.append(value)
            # if insert at the middle
            else:
                node = Node(value, curr.next)
                curr.next = node



    def pop(self):
        # Handle empty list
        if self.head.next is None:
            raise IndexError("Cannot pop from empty list")
        
        curr: Node = self.head.next

        # If one node in the list
        if curr.next is None:
            self.head.next = None
            self.tail = self.head
            return curr.value
        
        # If more than one node in the list
        while curr.next is not self.tail:
            curr = curr.next
        popped_node = self.tail
        curr.next = None
        self.tail = curr           # Point the self.tail to the new end node
        return popped_node.value
    


    def shift(self):
        # Handle empty list
        if self.head.next is None:
            raise IndexError("Cannot shift from empty list")
        
        shifted_node: Node = self.head.next
        self.head.next = shifted_node.next
        # if list had one node
        if shifted_node.next is None:
            self.tail = self.head
        # if list had more than one nodes
        else:
            shifted_node.next = None    # this is optional
        return shifted_node.value



    def remove(self, index):
        # if remove first element
        if index == 0:
            self.shift()
        else:
            i = 0
            curr: Node = self.head.next
            while i < index - 1 and curr.next is not None:
                i = i + 1
                curr = curr.next
            # If the while loop was broken because curr.next is None, then raise index error
            if curr.next is None:
                raise IndexError(f"Index {index} does not exist")
            # if remove last element
            elif curr.next is self.tail:
                self.pop()
            # if remove from middle
            else:
                removed_node: Node = curr.next
                curr.next = removed_node.next
                removed_node.next = None    # this is optional
                return removed_node.value
            


    def reverse(self):
        prev_node = self.head.next
        if prev_node is None:   # empty linked list
            return self
        
        curr_node = prev_node.next
        if curr_node is None:   # ll with one element
            return self
        
        next_node = curr_node.next
        if next_node is None:   # ll with two elements
            curr_node.next = prev_node
            prev_node.next = None
            self.head.next = curr_node
            self.tail = prev_node
            return self
        
        # if more than two elements
        while curr_node is not None:
            curr_node.next = prev_node  # swap the link
            # iterate the three pointers
            prev_node = curr_node
            curr_node = next_node
            if next_node is not None:
                next_node = next_node.next

        # swap the first and the last elements
        temp = self.head.next
        self.head.next = self.tail
        self.tail = temp

        self.tail.next = None
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
