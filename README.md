# Sorting-Time-Visualizer
Using Pyplot, displays and compares the sorting time between different sorting algorithms

The main code is within the sort_timer.py file, with the rest of the .py files as imported dependencies. When run, sort_timer.py will display - via Pyplot - a plotting chart comparing the sorting time between Bubble sort and Insertion sort. It will also display a plotting chart that shows the time it takes to find the mode within a data set is O(n). 

The time is measured using a simple sort_timer function that takes the difference between the time when the sorting functions start and end, with the sort_timer function used as decorator that wraps the sorting functions.

If you would like to compare using your own data sets or with different sorting algorithms, simply clone the repository and insert your data sets / algorithms into the sort_timer.py file.