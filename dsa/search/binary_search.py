def binary_search(array: list[int], item:int | None = None) -> bool:
    """Return True if item found, otherwise False."""
    if len(array)==0 or item == None:
        return False
    found=False
    lb=0
    ub=len(array)-1
    while not found and lb<=ub:
        mid = (lb+ub)//2
        if array[mid]==item:
            found=True
            break
        elif array[mid]> item:
            ub = mid - 1
        else:
            lb = mid + 1
    return found