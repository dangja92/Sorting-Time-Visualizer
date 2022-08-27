def insertion_sort(array):
    """
    Sort a list in ascending order using Insertion Sort
    :param array: a list of integers
    :return: None
    """
    for index in range(1, len(array)):
        value = array[index]
        pos = index - 1
        while pos >= 0 and array[pos] > value:
            array[pos + 1] = array[pos]
            pos -= 1
        array[pos + 1] = value