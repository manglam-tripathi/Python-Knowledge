#A function is a block of code that performs a specific task and can be reused.

#syntax of a function:
#def function_name(parameters):
def greet(name):
    print("Hello, " + name + "!")

#calling the function
greet("Alice")

#Returning values from a function
def add(a, b):
    return a + b    
result = add(5, 3)
print("The sum is: " + str(result))

#Scope of variables
x = 10  # Global variable

def foo():
    y = 5  # Local variable
    print(x)  # Can access global x
    print(y)  # Can access local y

foo()
print(x)  # OK
# print(y)  # Error: y is not defined outside foo()

#Conditional statements
#syntax of if statement:
#if condition:  
    #code to execute if condition is true
#elif another_condition:
    #code to execute if condition is false
#else:
    #code to execute if all conditions are false

num = 7
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


