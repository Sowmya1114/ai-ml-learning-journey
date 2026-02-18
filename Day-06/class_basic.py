##Day-7 Classes & Objects
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"My name is {self.name}, my age is {self.age}")
student=Student("raso",24)
student.greet()
