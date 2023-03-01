length = float(input("Enter the length : "))
breadth = float(input("Enter the breadth : "))

tri = lambda l, b: (1 / 2) * l * b
print(tri(length, breadth))
rec = lambda l, b: l * b
print(rec(length, breadth))
sqr = lambda l: l * l
print(sqr(length))
