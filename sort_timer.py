from matplotlib import pyplot
import time
import random
from functools import wraps
from hash_map_sc import *
from hash_map_oa import *


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
def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    Returns a tuple containing a DynamicArray containing the mode value(s) within "da" DynamicArray, and an integer
    that represents the highest frequency they appear.
    The input array "da" will contain at least one element, and all values stored in the array will be string.
    """
    hash_map = HashMap(len(da) // 3, hash_function_1)
    mode_val = DynamicArray()

    for i in range(len(da)):
        if hash_map.contains_key(da[i]):
            hash_map.put(da[i], hash_map.get(da[i]) + 1)
        else:
            hash_map.put(da[i], 1)

    max_freq = 0
    keys_list = hash_map.get_keys()

    for i in range(keys_list.length()):
        if hash_map.get(keys_list[i]) > max_freq:
            max_freq = hash_map.get(keys_list[i])

    for i in range(keys_list.length()):
        if hash_map.get(keys_list[i]) == max_freq:
            mode_val.append(keys_list[i])

    return mode_val, max_freq


def find_mode_timer(func1=find_mode):
    """
    Displays the time it takes to find the mode within a list of randomly generated integers between
    1 and 1000, with the sample sizes between 10,000 to 100,000 numbers for each data set.
    Using PyPlot, plot the number of integers on the X-axis and the time it takes to find the mode
    within the data set on the Y-axis, and displays the plot to the user
    @param: func1: default is the find_mode function
    """
    # create two lists that hold the sorting time for bubble sort vs insertion sort
    sort_time = []
    int_list_size = [num*1000 for num in range(1, 11)]  # holds the lists' size from 1000 to 10000

    # generate two identical lists of integers between range [1, 10000]
    for num in range(1, 11):
        # create a list of size equal to num * 1000
        list_1 = [random.randrange(1, 1000) for size in range(num*10000)]
        # call decorated bubble_sort and insertion_sort
        # to get sorting time and append time to each function's sort_time list
        sort_time.append(func1(list_1))

    # plot bubble sort's respective sorting times to the integers' lists size
    # x-axis = number of integers sorted, from 1000 to 10000
    # y-axis = sorting time in respect to integers' lists size
    pyplot.plot(int_list_size, sort_time, 'ro--', linewidth=2, label='Find Mode Big O')
    # plot insertion sort's respective sorting times to the integers' lists size
    pyplot.xlabel("Number of Integers")
    pyplot.ylabel("Sorting Time(seconds)")
    pyplot.legend(loc='upper left')
    pyplot.show()
    return


@sort_timer
def bubble_sort(a_list):
    """
    sort a list in ascending order using bubble sort
    :param a_list: a list
    :return: a sorted list in ascending order
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """
    sort a list in ascending order using insertion sort
    :param a_list: a list
    :return: a sorted list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(func1=bubble_sort, func2=insertion_sort):
    """
    compares the sorting time between two sorting functions for the same list of numbers
    ranging between 1000 to 10000 integers. The integers' range is 1 <= int <= 10000
    :param func1: bubble sort function
    :param func2: insertion sort function
    :return: a graph that compares func1 and func2 sorting time as the y-axis and the data sizes
    as the x-axis
    """
    # create two lists that hold the sorting time for bubble sort vs insertion sort
    bubble_sort_time = []
    insertion_sort_time = []
    int_list_size = [num*1000 for num in range(1, 11)]  # holds the lists' size from 1000 to 10000

    # generate two identical lists of integers between range [1, 10000]
    for num in range(1, 11):
        # create a list of size equal to num * 1000
        list_1 = [random.randrange(1, 10001) for size in range(num*1000)]
        list_2 = list(list_1)
        # call decorated bubble_sort and insertion_sort
        # to get sorting time and append time to each function's sort_time list
        bubble_sort_time.append(func1(list_1))
        insertion_sort_time.append(func2(list_2))

    # plot bubble sort's respective sorting times to the integers' lists size
    # x-axis = number of integers sorted, from 1000 to 10000
    # y-axis = sorting time in respect to integers' lists size
    pyplot.plot(int_list_size, bubble_sort_time, 'ro--', linewidth=2, label='Bubble Sort')
    # plot insertion sort's respective sorting times to the integers' lists size
    pyplot.plot(int_list_size, insertion_sort_time, 'go--', linewidth=2, label='Insertion Sort')
    pyplot.xlabel("Number of Integers Sorted")
    pyplot.ylabel("Sorting Time(seconds)")
    pyplot.legend(loc='upper left')
    pyplot.show()
    return


if __name__ == '__main__':
    # compare_sorts(func1=bubble_sort, func2=insertion_sort)
    find_mode_timer(func1=find_mode)
