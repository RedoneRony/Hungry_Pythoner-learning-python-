class Animal:
    def eat(self):
      print ("Eating...")
class Dog(Animal):
   def bark(self):
      print ("Barking...")
d=Dog()
d.eat()
d.bark()