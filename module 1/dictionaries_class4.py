# Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

d ={"Nick": "John", "count": 30, "place": "New York"}
e = {"name": "Alice", "age": 25, "city": "Los Angeles"}
f = dict(zip(d.keys(), e.values()))   # Creates a dictionary by zipping keys from d and values from e    
print(f)  # Output: {'a': 1, 'b': 2, 'c': 3}