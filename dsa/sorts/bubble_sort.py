def bubble_sort(array: list[int]) -> list[int]:
    """Sort the array in ascending order using bubble sort"""
    array = array.copy()
    swap=True
    while swap:
        swap=False
        for i in range(len(array)-1):
            if array[i]> array[i+1]:
                temp = array[i]
                array[i]=array[i+1]
                array[i+1]=temp
                swap=True
    return array
