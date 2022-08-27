def quick_sort(array, start, end):
    """
    Sort a list in ascending order using Quick Sort
    :param array: A list of integers
    :param start: starting index
    :param end: ending index
    :return: None
    """

    if start >= end:
        return

    def partition(array, start, end):
        """
        Return a partition index based on a pivot element
        :param array: list of integers
        :param start: starting index
        :param end: ending index
        :return: the partition index
        """

        pivot = array[end]
        p_index = start
        for i in range(start, end):
            if array[i] <= pivot:
                array[i], array[p_index] = array[p_index], array[i]
                p_index += 1
        array[p_index], array[end] = array[end], array[p_index]
        return p_index

    partition_index = partition(array, start, end)
    quick_sort(array, start, partition_index - 1)
    quick_sort(array, partition_index + 1, end)