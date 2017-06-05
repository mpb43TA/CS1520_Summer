"""
****** Indices and Slices ********
"""
some_list = [x for x in range(10)]
print(some_list)

print("The first index value")
print(some_list[1])

print("The last index value")
print(some_list[-1])

print("The second to last index value")
print(some_list[-2])

print("The indices 1 to 5(exclusive)")
print(some_list[1:5])

print("The indices less than 5")
print(some_list[:5])


line = "This is some text"
print(line)


print("The value at the 7th index position")
#PROBLEM Print the value at the 7th index

print("The characters from indices 4 to 9")
#PROBLEM Print the characters from indices 4 to 9 characters

print("The last 4 characters")
#Print the last 4 characters

"""
****** Iterators ********
"""

#PROBLEM Iterate through TWO ways "some_list" to add the values. Then print the result
 #1. Iterate through the indices (using range)
 
 #2. Iterate using the keyword "in"


#Dictionary Examples
dict1 = {"fruit":"apple", "vegetable":"carrot", "meat":"chicken"}
dict2 = {(1,2):"x", (1,3):"y", (4,5):"z"}

# for key in dict1:
#     print(key, dict1[key])
# 
# for key in dict2:
#     print(key, dict2[key])
# 
# for key1, key2 in zip(dict1,dict2):
#     print(key1, dict1[key1], key2, dict2[key2])

#Functions and Generators
#PROBLEM Define a function that will print the list, dict1, and dict2


# def print_gen(iterable):
#     for key in iterable:
#         yield key, iterable[key]
# 
# gen = print_gen(dict1)
# print(next(gen))
# for val in gen:
#     print(val)


