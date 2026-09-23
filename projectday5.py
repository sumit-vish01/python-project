#try to make a calculator using functions and learing betterment

a = int(input("Enter first  number "))
b = int(input("Enter second number "))
def add(a , b):
    return a + b

def different(a , b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error zero se divide nhi ho skta."
    return a / b


print("---Calculator Menu---")
print("1. Add(+)")
print("2. Subtract(-)")
print("3. Multiply(*)")
print("4. divide(/)")

choice = input("Enter your choice (1-4):")

if choice == "1":
    print("Result", add(a , b))
elif choice == "2":
    print("Result", add(a , b))
elif choice == "3":
    print("Result", add(a , b))
elif choice == "4":
     print("Result", add(a , b))
else:
    print("Invalid choice")
        
