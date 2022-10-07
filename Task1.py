class Rectangle:
    def __init__(self, len=1.0, wid=1.0):
        self.lenght = len
        self.width = wid

    def area(self):
        return self.width * self.lenght

    def perimeter(self):
        return 2 * (self.width + self.lenght)

    def get(self):
        return self.width , self.lenght

    def setter(self, len, wid):
        if (0 < len < 20) and (0 < wid < 20):
            self.lenght = len
            self.height = wid
        else:
            raise ValueError("Values out of range!")


x = Rectangle()
print(x.lenght, x.width)
prob = Rectangle(14.0 , 4.0)

print(prob.area())
print(prob.perimeter())
prob.lenght = 20.1
prob.width = 18
print(prob.lenght)
print(prob.width)
