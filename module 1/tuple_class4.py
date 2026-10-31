# Tuple is an ordered collection of elements, written in parentheses. Tuples are immutable, meaning their elements cannot be changed after creation.
# Tuples can hold elements of different data types, including integers, strings, and booleans. They are often used to group related data together.


# Converting list to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)


# Tuple operations and methods
# Indexing and slicing
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 5
print(my_tuple[1:4])  # Output: (2, 3, 4)

# concatenation
tuple1 = (1, 2, 3)  
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
tuple4 = tuple1 * 2
print(tuple4)  # Output: (1, 2, 3, 1, 2, 3)             

# Iterating through a tuple
t =("a", "b", "c")
for x in t :
    print(x)  # Output: a b c

    for i , x in enumerate(t):
        print(i, x)  # Output: 0 a, 1 b, 2 c   # indexing and value of the tuple

# Tuple unpacking
coordinates =[ (10.0, 20.0),(20.0, 30.0)]     
for x, y in coordinates:
    print(f"X: {x}, Y: {y}")   

# Zipping tuples
names = ("Alice", "Bob", "Charlie") 
numbers=(1, 2, 3)
zipped =zip(names,numbers)
print(tuple(zipped)) # Output: (('Alice', 1), ('Bob', 2), ('Charlie', 3))


 