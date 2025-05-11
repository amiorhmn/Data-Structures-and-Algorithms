def bubble_sort(arr: list) -> list:
    
    n: int = len(arr)

    # iterate through all positions of the list except the first position (as the first position will already be sorted when we sort the second position)
    # the sequence is iterated backward from last position to second position for ease of understanding (as after the first iteration of this loop the last position is sorted and so on)
    # For this outer for loop, range(n-1) is also a valid iterator
    for i in range(n-1, 0, -1):

        # variable to check if at least a pair of elements have swapped in current iteration
        has_swapped: bool = False

        # iterate from the first index to the previous index of current value of i (as the ith element will be compared when we get to i-1 index)
        # When range(n-1) is used for outer for loop, range(n-1-i) will be the iterator of this inner for loop
        for j in range(i-1):
            if arr[j+1] < arr[j]:
                # swap the elements
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

                has_swapped = True

        # if no swap happened in this iteration, the list is already completely sorted. No more iteration is needed
        if has_swapped == False:
            break

    return arr

# time complexity: O(n^2)