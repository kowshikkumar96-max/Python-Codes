n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0 or n == 1:
    print("Factorial is 1")
else:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print("Factorial is", fact)
