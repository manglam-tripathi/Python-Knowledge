user=input("What is your name?")
print("Hello " + user + "!")

print("Let's calculate the area and perimeter of a rectangle")
length = float(input("What is the length of the rectangle?"))
width = float(input("What is the width of the rectangle?")) 
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is " + str(area))
print("The perimeter of the rectangle is " + str(perimeter))
# In Python, you cannot concatenate a float directly with a string using the + operator. 

print("Lets make a temperature converter cONVERTING CELSIUS TO FAHRENHEIT")
celsius = float(input("What is the temperature in Celsius?"))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is " + str(fahrenheit))


print("lets calculate circle properties given the radius calculate the diameter, circumference and area of the circle")
radius = float(input("What is the radius of the circle?"))
diameter = 2 * radius
circumference = 2 * 3.14159 * radius
area = 3.14159 * radius ** 2
print("The diameter of the circle is " + str(diameter))
print("The circumference of the circle is " + str(circumference))
print("The area of the circle is " + str(area))

print("Lets make number classifier- Determine if a number is even or odd using the modulus operator")
number = int(input("What is the number?"))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print("LEts make a smart tip calculator- Calculate the tip amount based on the bill total and desired tip percentage")
bill_total = float(input("What is the total bill amount?"))
tip_percentage = float(input("What percentage would you like to tip?"))
tip_amount = bill_total * (tip_percentage / 100)
print("The tip amount is " + str(tip_amount))

print("Convert age in years to total days lived.")
age = int(input("What is your age in years?"))
total_days = age * 365.25  # accounting for leap years
print("You have lived for " + str(total_days) + " days.")

#Variable Swapper
print("Variable swapper: Swap the values of two variables without using a python tuple unpacking and other method also")
a = input("Enter the value of variable a: ")
b = input("Enter the value of variable b: ") 

print("Using a temporary variable")
temp = a
a = b
b = temp    
print("After swapping: a = " + a + ", b = " + b)

print("Using tuple unpacking")
a, b = b, a
print("After swapping: a = " + a + ", b = " + b)


print("Uing artihmetic operations to swap values")
a = a + b
b = a - b                       
a = a - b
print("After swapping: a = " + a + ", b = " + b)

print("Time Formatter: convert toatal seconds into hours:minute:seconds format ")
total_seconds = int(input("What is the total number of seconds?"))
hours = total_seconds // 3600 #1 hour = 60 minutes = 3600 seconds.
minutes = (total_seconds % 3600) // 60 #1 minute = 60 seconds, so we first find the remaining seconds after accounting for hours, and then divide by 60 to get the minutes.
seconds = total_seconds % 60 #Finally, we find the remaining seconds after accounting for both hours and minutes by taking the modulus of total_seconds with 60.
print("The time is " + str(hours) + ":" + str(minutes) + ":" + str(seconds))

#Anagrams
def are_anagrams(word1, word2):
    # If lengths are different, they can't be anagrams
    if len(word1) != len(word2):
        return False

    # Create dictionaries to count letters
    count1 = {}
    count2 = {}

    # Count letters in word1
    for letter in word1:
        if letter in count1:
            count1[letter] += 1
        else:
            count1[letter] = 1

    # Count letters in word2
    for letter in word2:
        if letter in count2:
            count2[letter] += 1
        else:
            count2[letter] = 1

    # Compare the two dictionaries
    return count1 == count2

# Example usage
w1 = "listen"
w2 = "silent"
if are_anagrams(w1, w2):
    print("They are anagrams!")
else:
    print("They are not anagrams.")

