# Data Structures

# List
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple

# Tuple
coordinates = (10.0, 20.0)
print(coordinates[1])  # Output: 20.0

# Dictionary
student = {"name": "John", "age": 21}
print(student["name"])  # Output: John

# Set
unique_numbers = {1, 2, 3, 2}
print(unique_numbers)  # Output: {1, 2, 3}


# List
# LIST is a collection of ordered ,mutable elements, written in square brackets
marks = [10, "abc", True] #mixed types: can hold ints ,strings ,boolen 
print(marks[1])


# List Membership
marks = [72, 85, 90, 85, 100, 85]
print(85 in marks)  # Output: True
print(60 not in marks)  # Output: True
print(marks.index(85))  # Output: 1
print(marks.count(85))  # Output: 2
if 100 in marks:
  print("topper")
else:
  print("no full marks")