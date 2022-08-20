# Sorting-Time-Visualizer
Using Matplotlib and timer as the decorator, displays and compares the sorting time between different sorting algorithms

The main code is within the sort_timer.py file, with the rest of the .py files as imported dependencies. When run, sort_timer.py will display - via Pyplot - a plotting chart comparing the sorting time between Bubble sort and Insertion sort.

The time is measured using a simple sort_timer function that takes the difference between the time when the sorting functions start and end, with the sort_timer function used as decorator that wraps the sorting functions.

Currently, this project supports the following sorting algorithms: Bubble Sort, Insertion Sort, Quicksort, and Merge Sort.

If you would like to compare using your own data sets or with different sorting algorithms, simply clone the repository and insert your data sets / algorithms into the sort_timer.py file.


**To Get Started**

Clone the repository to your directory. If you're using unix or Windows command line, simply navigate to your directory as follow:
```
cd <repository path>
```
Then, run the following command:
```
python3 sort_timer.py
```

Alternatively, you can use whichever editor (e.g. PyCharm, VSCode, etc....) to compile the sort_timer.py file instead. Happy coding!