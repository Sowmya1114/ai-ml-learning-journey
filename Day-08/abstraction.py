from abc import ABC,abstractmethod
class Shape(ABC):
  @abstractmethod 
  def area(self):
    pass
class Rectangle(Shape):
  def area(self):
    print("Area=Length*breadth")
class Circle(Shape):
  def area(self):
    print("Area=3.14*r^2")
r=Rectangle()
c=Circle()
r.area()
c.area()
