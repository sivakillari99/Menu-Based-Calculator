import math
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Not divisible by zero "
    else:
        return a/b
def modulus(a,b):
    return a%b
def square(a):
    return a**2
def square_root(a):
    if a<0:
        return "Square root of negative numbers is not possible"
    else:
        return math.sqrt(a)
def factorial(a):
    if a<0:
        return "Factorial not Possiblar for negative numbers"
    fact=1
    for i in range(1,a+1):
        fact*=1
    return fact
    
while True:
    print("\n CALCULATOR OPERATORS")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Power")
    print("7.Square")
    print("8.Square Root")
    print("9.Factorial")
    print("10.Exit")

    choice=int (input("Enter your choice: "))
    if choice==10:
        print("Thanks for using !")
        break
    
    if choice in [1, 2, 3, 4, 5, 6]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", add(a, b))

        elif choice == 2:
            print("Result =", subtract(a, b))

        elif choice == 3:
            print("Result =", multiply(a, b))

        elif choice == 4:
            print("Result =", divide(a, b))

        elif choice == 5:
            print("Result =", modulus(a, b))

        elif choice == 6:
            print("Result =", power(a, b))

    elif choice == 7:
        a = float(input("Enter a number: "))
        print("Result =", square(a))

    elif choice == 8:
        a = float(input("Enter a number: "))
        print("Result =", square_root(a))

    elif choice == 9:
        a = int(input("Enter a number: "))
        print("Result =", factorial(a))

        
