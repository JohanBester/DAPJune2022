def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)


num = input("Enter a positive number : ")

n = int(num)

# check if the number is negative
if n < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", factorial(n))
