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




ASSIGNMENT 3:

Module 4: Functions & Modules in Python 


Task 5: Calculate Factorial Using a Function 


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

CODE:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print("Factorial of", num, "is:", factorial(num))




Task 6: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

CODE:

import math

num = float(input("Enter a number: "))

sqrt_result = math.sqrt(num)
log_result = math.log(num)
sine_result = math.sin(num)

print("Square root:", sqrt_result)
print("Natural logarithm (ln):", log_result)
print("Sine (in radians):", sine_result)



ASSIGNMENT 4:

Module 5: Files, Exceptions, and Errors in Python
 
Task 7: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
 

PYTHON CODE:

try:
       with open("sample.txt", "r") as file:
        print("File content:\n")
        for line in file:
            print(line.strip())  
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")



Task 8: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.


PYTHON CODE:

text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.\n")

text_to_append = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.\n")

print("Final content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())



ASSIGNMENT 5:
Module 6: Data Structures and Strings in Python
 
Task 9: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

PYTHHON CODE:

student_marks = {
    "omkar": 85,
    "mayank": 92,
    "rahul": 78,
    "abhishek": 90,
    "chutka": 88
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")


Task 10: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list


PYTHON CODE:

numbers = list(range(1, 11))

first_five = numbers[:5]

reversed_first_five = first_five[::-1]

print("Original list of numbers:", numbers)
print("First five elements:", first_five)
print("Reversed extracted elements:", reversed_first_five)









    

























