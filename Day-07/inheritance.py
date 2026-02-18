class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print(f"My name is: {self.name}")
class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id=emp_id
    def show_id(self):
        print(f"My emp_id is: {self.emp_id}")
p=Employee("raso",1234)
p.show_name()
p.show_id()
