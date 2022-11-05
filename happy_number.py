# How to find a happy number:
# 1. Find the sum of the squares of the digits.
# 2. Repeat the process until the sum equals one.
# 3. If sum eventually reaches 1, the number is "happy". If not, it is "sad".
# 4. Use this method to create a function to determine if a number is happy or sad.

def get_sum_of_squares(n):

     sum = 0
     for digit in str(n):
        sum += int(digit) ** 2
     return sum
    
def happy_number(n):

    sum = get_sum_of_squares(n)
    while sum != 1:
        sum = get_sum_of_squares(sum)
        get_sum_of_squares(sum)
        if sum == 1:
            print(n, "is a happy number!")
        elif sum == 4:
            print(n, "is a sad number.")
            return False


n = 43
(happy_number(n))




