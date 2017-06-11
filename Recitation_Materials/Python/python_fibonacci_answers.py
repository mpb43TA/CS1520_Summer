#python generator example for Fibonacci taken from 
# http://pythoncentral.io/python-generators-and-yield-keyword/

import sys

#Fibonacci as a List
def fibonacci_list(n):
    counter = 2
    results = [1, 1]
    while counter < n:
        results.append(results[counter-1] + results[counter-2])
        counter += 1
    return results


#Fibonacci as a Generator        
def fibonacci_generator(n):
    curr = 1
    prev = 0
    counter = 0
    while counter < n:
        yield curr
        prev, curr = curr, curr + prev
        counter += 1

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
n = int(sys.argv[1])
print("Given sequence length: "+str(n))
gen = fibonacci_generator(n)
list = fibonacci_list(n)
print("Generator")
print_values(gen)
print("List")
print_values(list)
