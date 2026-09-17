def quick_sort(array: list[int]) -> list[int]:
    """Sort the array in ascending order using quick sort"""
    if len(array)<=1:
        return array
    pivot = array[len(array)//2]
    left=[]
    middle=[]
    right=[]
    for i in range(len(array)):
        if array[i]<pivot:
            left.append(array[i])
        elif array[i]>pivot:
            right.append(array[i])
        else:
            middle.append(array[i])
    return quick_sort(left) + middle + quick_sort(right)