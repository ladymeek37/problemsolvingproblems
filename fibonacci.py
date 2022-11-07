def fibonacci(nterms, n1):
    count = 0
    n2 = n1 + n1
    print("Fibonacci sequence:")
    print(n1)
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

fibonacci(10, (int(input("What number do you want to start your fibonacci sequence?  "))))