# python-assignments

Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division



PYTHON CODE:

a = float(input("enter the first no. : "))
b = float(input("enter the second no. : "))

Addition = a + b
Subtraction = a - b
Multiplication = a * b
Division = a / b

print("Addition : ",Addition)
print("Subtraction : ",Subtraction)
print("Multiplication : ",Multiplication)
print("Division : ",Division)



TASK 2:

Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.




python code:


a = input("enter your first name : ")
b = input("enter your last name : ")

print("hello" ,a +  b," welcome to the python program.")






ASSIGNMENT 2:
Module 3: Control Structures in Python


Task 3: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.




PYTHON CODE:

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is an Even number.")
else:
    print(number," is an Odd number.")



Task 4: Sum of Integers from 1 to 50 Using a Loop
 
Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.


PYTHON CODE:

x = 0

for i in range(1, 51):
    x += i  

print("The sum of numbers from 1 to 50 is:", x)




















