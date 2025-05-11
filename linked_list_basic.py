#################################################################
## No tail pointer and No dummy head, just a basic linked list ##
#################################################################

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

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



    def prepend(self, value):
        node = Node(value, self.head)
        self.head = node
            


    def append(self, value):
        node = Node(value, None)
        curr = self.head
        if curr is None: # check if empty
            self.head = node
        else:
            while curr.next is not None:   # loop until the end
                curr = curr.next
            curr.next = node
    

    
    def insert(self, index, value):
        if index == 0:  # if insertion at the start
            self.prepend(value)
        else:
            i = 0
            curr = self.head
            while i < index - 1 and curr is not None:   # loop until reaching index or the end
                i = i + 1
                curr = curr.next

            if curr is None:   # reached end but didn't find index
                raise IndexError(f"Cannot insert at index {index}")
            
            node = Node(value, curr.next)
            curr.next = node



    def shift(self):
        shifted = self.head

        if shifted is None:   # Handle empty list
            raise IndexError("Cannot shift from empty list")
        
        if self.head.next is None:  # If one node in the list
            self.head = None
        else:   # more than one node in the list
            self.head = self.head.next

        shifted.next = None     # remove dangling reference
        return shifted.value
    


    def pop(self):
        if self.head is None:   # Handle empty list
            raise IndexError("Cannot pop from empty list")
        if self.head.next is None:  # list has one node
            popped = self.head
            self.head = None
            return popped
        
        curr = self.head
        while curr.next.next is not None:   # loop until reaching index or the end
            curr = curr.next
        
        removed = curr.next
        curr.next = None

        return removed.value
    


    def remove(self, index):
        if index == 0:  # if removal at the start
            return self.shift()
        else:
            i = 0
            curr = self.head
            while i < index - 1 and curr is not None:   # loop until reaching index or the end
                i = i + 1
                curr = curr.next

            if curr is None or curr.next is None:    # reached the end
                raise IndexError(f"Index {index} does not exist")
            
            removed = curr.next
            curr.next = removed.next
            removed.next = None

            return removed.value
        


    def reverse(self):
        
        if self.head is None:   # empty linked list
            return self
        
        
        if self.head.next is None:   # ll with one element
            return self
        
        prev_node = self.head
        curr_node = prev_node.next
        prev_node.next = None

        if curr_node.next is None:   # ll with two elements
            curr_node.next = prev_node
            self.head = curr_node
            return self
        
        # if more than two elements
        next_node = curr_node.next
        while curr_node is not None:
            curr_node.next = prev_node  # swap the link
            # iterate the three pointers
            prev_node = curr_node
            curr_node = next_node
            if next_node is not None:
                next_node = next_node.next

        self.head = prev_node

        return self
    

# Time complexity:
# ---------------
# get_value   O(n)
# set_value   O(n)
# append      O(n)
# prepend     O(1)
# insert      O(n)
# pop         O(n)
# shift       O(1)
# remove      O(n)
# reverse     O(n)