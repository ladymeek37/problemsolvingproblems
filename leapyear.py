# Write a method that prints out the next 20 leap years:
#1. Google when the next leap year is.
#2. Print it to the console.
#3. Count + 1
#2. Add 4 to that year.
#3. Count + 2
# Contnue this method until the count reaches 20.

leap_year = 2024
count = 0
while count < 21:
    print (leap_year)
    count += 1
    leap_year = leap_year + 4