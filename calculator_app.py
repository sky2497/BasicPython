# Basic calculator

def add(a, b):
    answer = a + b
    print(str(a) +" + "+str(b) +" = "+ str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) +" - "+ str(b) +" = "+ str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) +" * "+ str(b) +" = "+ str(answer))

def div(a, b):
    answer = a / b
    print(str(a) +" / "+ str(b) +" = "+ str(answer))


print("A. Addition")
print("B. Substraction")
print("C. Multiplication")
print("D. Division")

choice = input("Enter your choice: ")

if choice == "A" or choice == "a":
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    add(a, b)
elif choice == "B" or choice == "b":
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    sub(a, b)

