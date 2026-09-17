from dsa.search.linear_search import linear_search
from dsa.search.binary_search import binary_search

#===============================
#        LINEAR SEARCH
#===============================

def test_linear_search():
    assert linear_search([1,4,2,3,5,7,3], 5) == True

def test_false_linear_search():
    assert linear_search([1,2,3,4,5,7,4],9) == False

def test_empty_linear_search():
    assert linear_search([], 5) == False
    assert linear_search([],) == False

def test_linear_search_first_element():
    assert linear_search([1,2,3,4,5,7,4],1) == True

def test_linear_search_last_element():
    assert linear_search([1,2,3,5,7,4],4) == True

def test_linear_search_large_dataset():
    data = list(range(1_000_000))
    assert linear_search(data, 999_999) == True

def test_linear_search_large_dataset_not_found():
    data = list(range(1_000_000))
    assert linear_search(data, 1_000_000) == False


#===============================
#        BINARY SEARCH
#===============================

def test_binary_search():
    assert binary_search([1,2,3,4,5,6,7,8,9], 5) == True

def test_false_binary_search():
    assert binary_search([1,2,3,4,5,6,7,8],9) == False

def test_empty_binary_search():
    assert binary_search([], 5) == False
    assert binary_search([],) == False

def test_binary_search_first_element():
    assert binary_search([1,2,3,4,5,6,7,8,9],1) == True

def test_binary_search_last_element():
    assert binary_search([1,2,3,4,5,6,7,8,9],9) == True

def test_binary_search_large_dataset():
    data = list(range(1_000_000))
    assert binary_search(data, 999_999) == True

def test_binary_search_large_dataset_not_found():
    data = list(range(1_000_000))
    assert binary_search(data, 1_000_000) == False