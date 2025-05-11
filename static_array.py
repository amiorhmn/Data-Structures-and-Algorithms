class StaticArray:
    def __init__(self, capacity):
        self.arr = [None]*capacity
        self.capacity = capacity
        self.length = 0

    def __repr__(self):
        return f"{self.arr}"
    
    def insert_end(self, item):
        if self.length < self.capacity:
            self.arr[self.length] = item
            self.length += 1
        else:
            raise OverflowError("Cannot insert item: Maximum capacity reached")
        
    def insert_middle(self, index, item):
        if self.length == self.capacity:
            raise OverflowError("Cannot insert item: Maximum capacity reached")
        if index >= self.capacity:
            raise IndexError(f"Cannot insert item: Index {index} does not exist")
        for i in range(self.length-1, index-1, -1):
            self.arr[i+1] = self.arr[i]
        self.arr[index] = item
        self.length += 1

    def remove_end(self):
        if self.length == 0:
            raise IndexError("Cannot remove item: Array already empty")
        self.arr[self.length-1] = None
        self.length -= 1

    def remove_middle(self, index):
        if self.length == 0:
            raise IndexError("Cannot remove item: Array already empty")
        if index >= self.length:
            raise IndexError(f"Cannot remove item: No item in index {index}")
        for i in range(index+1, self.length):
            self.arr[i-1] = self.arr[i]
        self.arr[self.length-1] = None
        self.length -= 1



# Time complexity:
# ---------------
# insert_end O(1)
# insert_middle O(n)
# remove_end O(1)
# remove_middle O(n)