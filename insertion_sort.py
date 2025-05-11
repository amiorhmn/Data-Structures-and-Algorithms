def insertion_sort(arr: list) -> list:
    
    n: int = len(arr)

    # as the list of one element (the first element) is already sorted, we start from the second element (list of two elements)
    for i in range(1, n):
        # starting from the current ith element, compare it with its previous element, iteratively until there is no more element left at the start or the pair is correctly sorted
        j = i
        while arr[j] < arr[j-1] and j > 0:
            # swap the elements
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j = j - 1
    
    return arr

# time complexity: O(n^2)