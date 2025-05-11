class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    


# Time complexity:
# ---------------
# push O(1)
# pop O(1)

# Stack is implemented using Dynamic Array, so there is a pointer for the last element
# (i.e. there is arr.length property that can be used to access the last element in constant time)
