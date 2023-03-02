class Rectangle:

    length = 0
    breadth = 0

    def __init__(self):
        self.length = float(input("Enter the length : "))
        self.breadth = float(input("Enter the breadth : "))

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def __cmp__(self, other):
        if self.area() > other.area():
            res = f"{self.area()} is greater"
            return res
        elif self.area() == other.area():
            res = f"both have same area = {self.area()}"
            return res
        else:
            res = f"{other.area()} is greater"
            return res


rec1 = Rectangle()
print("Area of rectangle 1 = ", rec1.area())
print(rec1.perimeter())


rec2 = Rectangle()
print("Area of rectangle 2 = ", rec2.area())
print(rec2.perimeter())

print(rec1.__cmp__(rec2))


