from abc import ABC, abstractmethod


class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

class Rectangle(Shape):
     def area(self,l,b):
        self.area = l*b
        print(f"Area of the Rectangle is: {self.area}")


class Square(Shape):
    def area(self, l):
        self.area = l * l
        print(f"Area of the Square is: {self.area}")


class Triangle(Shape):
    def area(self, l, b):
        self.area = (l * b)/2
        print(f"Area of the Triangle is: {self.area}")


rec = Rectangle()
rec.area(3,4)
sq = Square()
sq.area(5)
tri=Triangle()
tri.area(6,7)


