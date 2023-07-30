math = input("Expresion:").strip()

x, y, z = math.split(" ")

n1 = float(x)
n2 = float(z)

if y == "+":
    result = n1+n2
    print(f"{result:.1f}")
elif y == "-":
    result = n1-n2
    print(f"{result:.1f}")
elif y == "*":
    result = n1*n2
    print(f"{result:.1f}")
elif y == "/":
    result = n1/n2
    print(f"{result:.1f}")
