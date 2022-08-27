def bubble_sort(array):
    """
    Sort a list in ascending order using Bubble Sort
    :param array: a list of integers
    :return: None
    """
    for pass_num in range(len(array) - 1):
        for index in range(len(array) - 1 - pass_num):
            if array[index] > array[index + 1]:
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp

