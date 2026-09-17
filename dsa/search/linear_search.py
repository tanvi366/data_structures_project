def linear_search(array: list[int], item:int | None = None) -> bool:
    """Return True if item found, or False if not found"""
    if len(array)==0 or item == None:
        return False
    i=0
    while array[i]!=item and (i+1<len(array)):
        i+=1
    if array[i]==item:
        return True
    else:
        return False