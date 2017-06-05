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

#1 On the CLI provide an index to extend the fibonacci sequence

n = sys.argv[1]

gen = fibonacci_generator(n)
list = fibonacci_list(n)

print_values(gen)
print_values(list)
