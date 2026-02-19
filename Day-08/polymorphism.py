class Dog:
  def sound(self):
    print("Dog barks")
class Cat:
  def sound(self):
    print("Cat meows")
animal=[Dog(),Cat()]
for a in animal:
    a.sound()
