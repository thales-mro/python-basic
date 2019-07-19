def divides(a, b):
    try:
        result = a/b
        print(result)
    except ZeroDivisionError:
        print("Can't divide by zero")

divides(1, 1)
divides(1, 0)
