Cameron Rogers 
29/04/2024 
Software Engineer Coding Project - Genome Regions 
Completed in one afternoon ~ half a day.

This project can be run as a standard python file: 'python .\analysis.py'. 
It assumes that the input files provided are present and error-free. If Matplotlib is installed, then graphs can be produced for reference.

Requirements
Python 3.x
Matplotlib (optional for plotting)

Installation
Download the files.
Ensure that Python 3.x is installed.
(Optional) Install Matplotlib for graphical output.

Usage
Run python .\analysis.py in the project directory.

Algorithm
The algorithm used in part one uses a heap to provide an efficient way to keep track of the regions. 
It first initialises this heap and a list that will store each region provided along with the row number that it should be assigned. 
Next, it iterates over each region provided by the input file and checks if the lowest end position in the heap is smaller than the region in question. 
If so, this region does not overlap so the position can be popped from the heap. The end position of the current region is added to the heap, regardless of the previous check. 
Finally, the output list rows is appended with a tuple containing the region coordinates and the row number which is equal to the heap size -1. 
A while loop is used so that the row height can reduce if there is space for it.

The algorithm in part two counts the overlapping regions using a linear scan to work through the dataset in order. 
First, the events are created for the algorithm to scan through. These are the start and end points of each region and have an event type to show if a region is beginning or ending. 
As the algorithm scans through the events, a counter keeps track of the current number of overlapping regions incrementing and decrementing for the relevant type. 
A segment is added when the coordinate is changed and there is already a segment started as indicated by the counter. 
The segment is assigned the counter to record the number of overlapping regions it represents.

I plotted the output to be able to have a visual reference to the data as it is difficult to contextualise the large integer coordinates and an output graph was already provided.