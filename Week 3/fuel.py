while True:
    fuel = input("Frctions:")

    try:
        x,y = fuel.split("/")
        x = int(x)
        y = int(y)
        p = x / y
        if p <= 1 :
            break
    except(ValueError, ZeroDivisionError):
        pass

fuel = int(p*100)
if fuel <= 1:
    print("E")
elif fuel >= 99:
    print("F")
else:
    print(f"{fuel}%")




