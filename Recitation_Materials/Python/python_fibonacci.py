#python generator example for Fibonacci taken from 
# http://pythoncentral.io/python-generators-and-yield-keyword/

import sys

#Fibonacci as a List
def fibonacci_list(n):
    """
    Return the fibonnaci set as a list 
    """


#Fibonacci as a Generator        
def fibonacci_generator(n):
    """
    Implement a generator for computing Fibonacci the Fibonacci sequence
    """

#Print Iterable
def print_values(iterable):
    for val in iterable:
        print(val)

"""
Fibonacci Sequence
1, 1, 2, 3, 5, 8, 13, ...
x_i = x_i-1 + x_i-2, for all i greater than 1
x_0, x_1 = 1
NOTE: underscore is to signify that the following is a subscript
"""

#1 On the command line, provide the last desired sequence value
n = sys.argv[1]
print("Given sequence length: "+str(n))
# gen = fibonacci_generator(n)
# list = fibonacci_list(n)
# 
# print_values(gen)
# print_values(list)
