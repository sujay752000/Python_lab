class Rectangle:
    length = 0
    breadth = 0
    area = 0

    def __init__(self, len, bre):
        self.length = len
        self.breadth = bre

    def perimeter(self):
        self.area = 2 * (self.length + self.breadth)
        return self.area

rec1 = Rectangle(5, 10)
rec2 = Rectangle(6, 10)

if(rec1.perimeter() > rec2.perimeter()):
    print(f"{rec1.perimeter()} is greater")
elif(rec1.perimeter() == rec2.perimeter()):
    print(f"both are same : {rec1.perimeter()}")
else:
    print(f"{rec2.perimeter()} is greater")