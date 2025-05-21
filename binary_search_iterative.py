# returns the index if target is found otherwise returns -1
# input list must be sorted

def binary_search(li: list[int | float], target: int | float) -> int:
    lo = 0
    hi = len(li) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target < li[mid]:
            hi = mid - 1
        elif target > li[mid]:
            lo = mid + 1
        else:
            return mid
    return -1