# Prime Numbers
# A prime number is a number that is only divisible by one and itself.
# b. Write a method that prints out all prime numbers between 1 and 100

#1. Write a function the determines if a number is divisible by 1 and itself (prime).
#2. In the function, if it is prime, print it.
#3. Find a way to do this 1-100.


def is_prime(num):
# If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                break
        else:
            print(num)
    else:
        print(num, "is not a prime number")

for num in range(2, 100, 1):
    is_prime(num)
    
