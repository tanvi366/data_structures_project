def insertion_sort(array: list[int]) -> list[int]:
    """Sort the array in ascending order using insertion sort"""
    array = array.copy()
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            temp = array[j]
            array[j]=array[j-1]
            array[j-1]=temp
            j=j-1
    return array