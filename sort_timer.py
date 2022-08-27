from matplotlib import pyplot
import time
import random
from functools import wraps
from bubble_sort import *
from insertion_sort import *
from quick_sort import *
from merge_sort import *


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


bubble_sort = sort_timer(bubble_sort)
insertion_sort = sort_timer(insertion_sort)
quick_sort = sort_timer(quick_sort)
merge_sort = sort_timer(merge_sort)


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
    int_list_size = [num*1000 for num in range(1, 101)]  # holds the lists' size from 1,000 to 1,000,000

    # generate four identical lists of integers between range [1, 1,000,000]
    for num in range(1, 101):
        # create a list of size equal to num * 1000
        list_1 = [random.randrange(1, 1000000) for size in range(num*100)]
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
