# my first calculator
x = input("x: ")
op = input("which operator: ").strip()
y = input("y: ")
a = float(x)
b = float(y)

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    if b == 0:
        print("ERROR: Division by zero")
    else:
        print(a/b)
else:
    print("Unknown operator.")
