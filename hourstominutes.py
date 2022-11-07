# Write a method that converts a given number to hours and minutes:
# 1. Ask user to input a number.
# 3. Divide that number by 60.
# 4. The whole number is the hours. The remainder is the minutes.
# 5. Print it to the console.

number = 180
hours = number // 60
minutes = number % 60

print("Hours:", hours, "Minutes:", minutes)