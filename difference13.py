# Write a method to get the difference between a given number and 13, if the number is
# greater than 13 return double the absolute difference.
# 1. Get the difference between a given number and 13.
# 2. Store that value in a variable.
# 3. Create an if statement to see if the value is greater than 13.
# 4. If so, double that value.

number = int(input("Pick a number:"))
total = number - 13
if total > 13:
    total = total * 2
    print (total)
elif total < 13:
    print ("Your number is too low.")

