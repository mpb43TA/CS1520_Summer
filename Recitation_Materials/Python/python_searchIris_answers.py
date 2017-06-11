#python generator example for Fibonacci taken from 
# http://pythoncentral.io/python-generators-and-yield-keyword/
import sys
def search(keyword, index, thresh, file):
    """
    Change this function to a generator
        - The index points to the value in the line that is being 
            compared to the threshold
        - The value at the index in the string is printed 
            if it is greater than or equal to the threshold
        - The keyword is the last index (i.e Iris-<type>)
    """
    print('generator for ' + keyword)
    f = open (file, 'r')
    for line in f:
        line = line.rstrip()
        line_split = line.split(',')
        #check the keyword of the line
        #check that the value is greater than equal threshold
        if line_split[-1] == keyword and float(line_split[index])>=thresh:
            yield line


#Print Iterable
def print_values(iterable):
    for val in iterable:
        print(val)
"""
#1 Read through the file filtering based on the threshold and keyword
    - will have to change such that search is a generator
#2 Loop through a set of tuples where each keyword (iris type) 
    is associated with a value and threshold value (i.e. (<keyword>, <value>))
#3 use print_values to display your result
"""

file = sys.argv[1]
index = 0
threshold = 6.5
keyword = 'Iris-versicolor'
gen = search(keyword, index, threshold, file)
print_values(gen)


