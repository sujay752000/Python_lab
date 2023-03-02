class Rectangle:

    length = 0
    breadth = 0

    def __init__(self):
        self.length = float(input("Enter the length : "))
        self.breadth = float(input("Enter the breadth : "))

    def area(self):
        return self.length * self.breadth

    def __lt__(self, others):
        if self.area() < others.area():
            res = f"{self.area()} less than {self.area()}"
            return res
        elif others.area() < self.area():
            res = f"{others.area()} less than {self.area()}"
            return res
        else:
            res = f"both have same area {self.area()}"
            return res


rec1 = Rectangle()
print("Area of rectangle 1 = ", rec1.area())

rec2 = Rectangle()
print("Area of rectangle 2 = ", rec2.area())

print(rec1 < rec2)