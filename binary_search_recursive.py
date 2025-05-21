# returns the index if target is found otherwise returns -1
# input list must be sorted

def binary_search(li: list[int | float], target: int | float, lo: int | None = None, hi: int | None = None) -> int:
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(li) - 1
    mid = (lo + hi) // 2
    if lo > hi:
        return -1
    if li[mid] == target:
        return mid
    if li[mid] > target:
        return binary_search(li, target, lo=lo, hi=mid-1)
    if li[mid] < target:
        return binary_search(li, target, lo=mid+1, hi=hi)