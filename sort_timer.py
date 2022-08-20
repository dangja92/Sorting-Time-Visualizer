from matplotlib import pyplot
import time
import random
from functools import wraps


def sort_timer(func):
    """
    decorates a function with a wrapper that calculates how long it takes to execute function
    :param func: a function
    :return: function decorated with wrapper
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        time_sorted = end - start
        return time_sorted

    return wrapper


@sort_timer
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


@sort_timer
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


@sort_timer
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


@sort_timer
def merge_sort(arr):
    """
    Sorts an array using Merge Sort
    :param arr: list of integers
    :return: None
    """

    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        merge_sort(L)
        # Sorting the second half
        merge_sort(R)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def compare_sort_time(func1=bubble_sort, func2=insertion_sort, func3=quick_sort, func4=merge_sort):
    """
    Compares the sorting time between all 4 different sorting algorithms over a sample size of 1000 to 20000
    randomly generated integers. The sorting times are plotted and displayed for each algorithm
    :param func1: Bubble Sort
    :param func2: Insertion Sort
    :param func3: Quick Sort
    :param func4: Merge Sort
    :return: A graph showing the sorting time differences between all 4 algorithms
    """
    # create lists to hold sorting time for each algorithm
    bubble_sort_time = []
    insertion_sort_time = []
    quick_sort_time = []
    merge_sort_time = []
    int_list_size = [num*1000 for num in range(1, 1001)]  # holds the lists' size from 1,000 to 1,000,000

    # generate four identical lists of integers between range [1, 1,000,000]
    for num in range(1, 1001):
        # create a list of size equal to num * 1000
        list_1 = [random.randrange(1, 1000001) for size in range(num*1000)]
        list_2 = list(list_1)
        list_3 = list(list_1)
        list_4 = list(list_1)

        # call decorated sorting functions to get sorting time. Append time to each function's sort_time list
        bubble_sort_time.append(func1(list_1))
        insertion_sort_time.append(func2(list_2))
        quick_sort_time.append(func3(list_3, start=0, end=(len(list_3)-1)))
        merge_sort_time.append(func4(list_4))

    # plot bubble sort's respective sorting times to the integers' lists size
    # x-axis = number of integers sorted, from 1000 to 20000
    # y-axis = sorting time in respect to integers' lists size
    pyplot.plot(int_list_size, bubble_sort_time, color='red', marker='o', linestyle='dashed', linewidth=2, label='Bubble Sort')
    # plot insertion sort's respective sorting times to the integers' lists size
    pyplot.plot(int_list_size, insertion_sort_time, color='green', marker='o', linestyle='dashed', linewidth=2, label='Insertion Sort')
    # plot quick sort's respective sorting times to the integers' lists size
    pyplot.plot(int_list_size, quick_sort_time, color='yellow', marker='o', linestyle='dashed', linewidth=2, label='Quick Sort')
    # plot merge sort's respective sorting times to the integers' lists size
    pyplot.plot(int_list_size, merge_sort_time, color='purple', marker='o', linestyle='dashed', linewidth=2, label='Merge Sort')

    pyplot.xlabel("Number of Integers Sorted")
    pyplot.ylabel("Sorting Time(seconds)")
    pyplot.legend(loc='upper left')
    pyplot.show()
    return


if __name__ == '__main__':
    compare_sort_time(func1=bubble_sort, func2=insertion_sort, func3=quick_sort, func4=merge_sort)
