#Created By - Harshit Arora
#Task 2 CODSOFT 

#DESIGN A SIMPLE CALCULATOR WITH BASIC ARITHMETIC OPERATIONS.
#PROMPT THE USER TO INPUT TWO NUMBERS AND AN OPERATION CHOICE.
#PERFORM CALCULATION AND DISPLAY THE RESULT.

print("SIMPLE CALCULATOR")
#Function To Perform Addition
def add(a,b):
    return a + b

#Function To Perform Subtraction
def subtract(a,b):
    return a - b

#Function To Perform Multiplication
def multiply(a,b):
    return a * b

#Function To Perform Division
def divide(a,b):
        if b != 0:
             return a / b
        else:
             return "Error! Division By 0."
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    first_num = float(input("Please enter the first number: ")) #taking Number 1 as input from the user
    operator = input("Please choose the operator (+,-,*,/): ") #taking operator as input from the user
    second_num = float(input("Please enter the second number: ")) #taking Number 2 as input from the user
#Using Conditional If-Else statements
    if operator in operations:
        result = operations[operator](first_num,second_num)
    else:
        result = "Please choose a valid operator!"
    print(f"The result is: {result}")
calculator()



