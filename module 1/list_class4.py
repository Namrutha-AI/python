#List bounds (maximum index number) is always one less than the number of elements in the list. (for loop should not exceed the index number

list =[10,20,30]
print(list[0])  # Output: 10
print(list[1])  # Output: 20
print(list[2])  # Output: 30    
print(list[-1 ])

print(list[1:2])  # Output: [20] #slicing of list

n =[0,1,2,3,4,5,6,7,8,9]
print(n[2:5])  # Output: [2, 3, 4] 

print(n[:3])  # Output: [0, 1, 2]
print(n[-3:10])  # Output: [7, 8, 9]

#SLICING - Reverse
print(n[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#copying a list
list1 = [1, 2, 3]
list2 = list1.copy()  # Creates a shallow copy of the list

#Replace
list1[0] = 10
print(list1)  # Output: [10, 2, 3]  

#Delete
del list1[1]    
print(list1)  # Output: [10, 3]  

#Insert
list1.insert(1, 20)  # Inserts 20 at index 1
print(list1)  # Output: [10, 20, 3]  


# List Elements Removal 
list = [1, 2, 3, 4, 5]
list.remove(5)
print(list)  # Output: [1, 2, 3, 4]


# pop () method
list =[1,2,3,4,5]
list.pop(2)
print(list)  # Output: [1, 2, 4, 5] 


# Removing items while looping
nums =[1, 2, 3, 4, 5]
for n in nums:
    if n==2:
        nums.remove(n)
print(nums)  # Output: [1, 3, 4, 5] 


#List Method () -Adding and searching the elements in the list

list =[98,98,97,96,95]
list.append(89)  # Adds 89 at the end of the list
print(list)  # Output: [98, 98, 97, 96, 95, 89]


#Extend method - used to add multiple elements to the end of a list
list1 =[1,2,3]
list2 =[4,5,6]
list1.extend(list2) 
print(list1)  # Output: [1, 2, 3, 4, 5, 6] 


# List sorting
list =[5, 2, 9, 1, 5, 6]
list.sort()
print(list)  # Output: [1, 2, 5, 5, 6, 9]

list.sort(reverse=True)
print(list)  # Output: [9, 6, 5, 5, 2, 1]

# Nested Lists
nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2])  # Output: 6