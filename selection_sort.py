def selection_sort(arr: list) -> list:
    
    n: int = len(arr)

    # iterate through all positions of the list except the last position
    for i in range(n-1):
        min_idx = i
        # compare the element of the current position with every succeeding element to find the minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # if current element is not the minimum, swap its position with the minimum
        if min_idx != i:
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp

    return arr

# time complexity: O(n^2)