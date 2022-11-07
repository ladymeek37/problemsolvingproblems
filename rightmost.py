#Write a method to check from three given numbers (non negative integers) that two or all of them have the same rightmost digit.
#1. Access the string representation of the first number.
#2. Get the last character of the string representation.
#3. Convert the character to an integer.

number1 = 5271
number2 = 3323
number3 = 1233
n1 = int(repr(number1)[-1])
n2 = int(repr(number2)[-1])
n3 = int(repr(number3)[-1])

if n2 == n3 and n1 == n3 and n1 == n2:
    print (number1, ",", number2, ", and", number3, "all have the same rightmost numbers")
elif n1 == n3:
    print (number1, "has the same rightmost as", number3)
elif n1 == n2: 
    print (number1, "has the same rightmost as", number2)
elif n2 == n3:
    print (number2, "has the same rightmost as", number3)
else: 
    print("None of the numbers have the same rightmost.")





