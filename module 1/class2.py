#Indentation and code blocks

age =30 
if age>25:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


#Variable 
age =21
price = 29.99
PI = 3.1415
a, b, c = 1, 2, 3
a, b = b, a #swapping the values
print(a, b)
print(age, price, PI)



# Datatypes

n = 2**100
print(n)

#float 

f = 0.1 + 0.3
print(f)

#Indexing 

s = "python"
print(s[0], s[-1], s[1:4])


#Types of Expression 

a,b =10 ,20
print(a*b+2)  #output 26 #arithmatic expression

print(a>b)  #output False #relational expression

print(a==b)  #output False #relational expression
print(a!=b) 
 #output True #relational expression
print("hi"+" there")

#boolen 

print(5>3)
print(bool(1))
print(bool(0)) 



#Conditional Statements
 #if -else statement
temp = 38
if temp > 37:
    print("fever")
    print("Check Fever")
else:
    print("No fever") 

#elif statement
marks = 72
if marks >= 90:
   print("Grade A")
 
elif marks >= 60:
    print("Grade B")
 
else:
    print("Grade C")



#Nested Conditions:

marks,attendence =85 ,80
if marks >= 80:
    if attendence >= 85:
        print("Grade A")
    else:
        print("Fail due to low attendance")

else:
    print("Grade C")


# Pass statement 
for n in range(5):
    if n%2 ==0:
        pass
else:
    print(n)

def todo():
    pass