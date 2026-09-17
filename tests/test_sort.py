import pytest
from dsa.sorts.bubble_sort import bubble_sort
from dsa.sorts.merge_sort import merge_sort
from dsa.sorts.insertion_sort import insertion_sort
from dsa.sorts.quick_sort import quick_sort

SORTING_ALGORITHMS = [bubble_sort, merge_sort, insertion_sort, quick_sort]

@pytest.mark.parametrize("sort_algorithm", SORTING_ALGORITHMS)
def test_empty(sort_algorithm):
    assert sort_algorithm([]) == []

@pytest.mark.parametrize("sort_algorithm", SORTING_ALGORITHMS)
def test_random(sort_algorithm):
    assert sort_algorithm([1,3,2,4,6,5,7,8,9]) == [1,2,3,4,5,6,7,8,9]

@pytest.mark.parametrize("sort_algorithm", SORTING_ALGORITHMS)
def test_sorted(sort_algorithm):
    assert sort_algorithm([1,2,3,4,5]) == [1,2,3,4,5]

@pytest.mark.parametrize("sort_algorithm", SORTING_ALGORITHMS)
def test_reverse(sort_algorithm):
    assert sort_algorithm([5,4,3,2,1]) == [1,2,3,4,5]

@pytest.mark.parametrize("sort_algorithm", SORTING_ALGORITHMS)
def test_single(sort_algorithm):
    assert sort_algorithm([4]) == [4]

@pytest.mark.parametrize("sort_algorithm", SORTING_ALGORITHMS)
def test_duplicates(sort_algorithm):
    assert sort_algorithm([1,2,3,4,4,5,3,4,2]) == [1,2,2,3,3,4,4,4,5]

@pytest.mark.parametrize("sort_algorithm", SORTING_ALGORITHMS)
def test_all_duplicates(sort_algorithm):
    assert sort_algorithm([4,4,4,4]) == [4,4,4,4]

@pytest.mark.parametrize("sort_algorithm", SORTING_ALGORITHMS)
def test_negative(sort_algorithm):
    assert sort_algorithm([-1,5,2,-3,4]) == [-3,-1,2,4,5]

@pytest.mark.parametrize("sort_algorithm", SORTING_ALGORITHMS)
def test_large(sort_algorithm):
    data = list(range(1000, 0, -1))
    assert sort_algorithm(data) == list(range(1,1001))

@pytest.mark.parametrize("sort_algorithm", SORTING_ALGORITHMS)
def test_sort_is_ascending(sort_algorithm):
    data = [1,4,2,3,6,5,7,9,8]
    result = sort_algorithm(data)
    assert result == sorted(result)

@pytest.mark.parametrize("sort_algorithm", SORTING_ALGORITHMS)
def test_sort_preserves_elements(sort_algorithm):
    data = [1,4,2,3,6,5,7,9,8]
    result = sort_algorithm(data)
    assert sorted(result) == sorted(data)

@pytest.mark.parametrize("sort_algorithm", SORTING_ALGORITHMS)
def test_sort_does_not_modify_input(sort_algorithm):
    data = [1,4,2,3,6,5,7,9,8]
    original = data.copy()
    sort_algorithm(data)
    assert data == original
