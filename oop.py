# in OOP, a class is a blueprint or template for creating objects, while an object is an instance of a class. A class defines a set of attributes and methods that are common to all objects of that class. Attributes are variables that hold data, while methods are functions that operate on that data.

# Let's take a simple example of a class and object to illustrate the concept of OOP:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#         print("Hello, my name is", self.name, "and I am", self.age, "years old.")

# create an object of the Person class
# p = Person("John", 30)

# call the say_hello() method on the object
# p.say_hello()


# In this example, we define a Person class with two attributes, name and age, and one method, say_hello(). The __init__() method is a special method that is called when an object of the class is created, and it initializes the object's attributes.

# We then create an object of the Person class, p, and pass in the arguments "John" and 30 to the __init__() method to initialize the object's attributes. Finally, we call the say_hello() method on the object p, which prints out a message to the console.

# This is just a simple example of OOP, but it illustrates the basic concept of classes and objects. In practice, OOP can be used to build complex systems with many interacting objects and classes. Some other key concepts in OOP include inheritance, encapsulation, and polymorphism.





# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_make(self):
#         return self.make

#     def get_model(self):
#         return self.model

#     def get_year(self):
#         return self.year

# # create an object of the Car class
# car = Car("Toyota", "Corolla", 2022)

# # print the car's make, model, and year
# print("Make:", car.get_make())
# print("Model:", car.get_model())
# print("Year:", car.get_year())

# In this example, we define a Car class with three attributes, make, model, and year, and three methods, get_make(), get_model(), and get_year(). The __init__() method is a special method that is called when an object of the class is created, and it initializes the object's attributes.

# We then create an object of the Car class, car, and pass in the arguments "Toyota", "Corolla", and 2022 to the __init__() method to initialize the object's attributes. Finally, we call the get_make(), get_model(), and get_year() methods on the object car, which print out the car's make, model, and year to the console.

# inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# # create objects of the Dog and Cat classes
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# # call the speak() method on the objects
# print(dog.name, "says", dog.speak())
# print(cat.name, "says", cat.speak())
# In this example, we define an Animal class with one attribute, name, and one method, speak(), which is defined as a pass statement (meaning it does nothing). We also define two subclasses of Animal: Dog and Cat. Each subclass overrides the speak() method to return a different string.

# We then create objects of the Dog and Cat classes, dog and cat, respectively. Finally, we call the speak() method on each object, which returns the appropriate string based on the class of the object.


# Example 3: Polymorphism

# ruby
# Copy code
# class Shape:
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length ** 2

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# # create objects of the Square and Circle classes
# square = Square(5)
# circle = Circle(3)

# # print the areas of the objects
# print("Area of square:", square.area())
# print("Area of circle:", circle.area())
# # In this example, we define a Shape class with one method, area(), which is defined as a pass statement. We also define two subclasses of Shape: Square and Circle. Each subclass overrides the area() method to calculate

# import math
# class ab():
#     def area(self,r):
#         return math.pi*r**2
# b=ab()
# r=int(input())
# print(b.area(r))

# class vehicle():
#     def __init__(self,name,wheel,sit):
#         self.name=name
#         self.wheel=wheel
#         self.sit=sit
#     def getname(self):
#         return self.name
#     def getwheel(self):
#         return self.wheel
#     def getsit(self):
#         return self.sit
# b=vehicle('toyota',8,6)
# print(b.getname())
# print(b.getsit())
# print(b.getwheel())


class family():
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def getstd(self):
        return self.std
b=family("ankit",21,"b.tech")
print(b.getage())
print(b.getname())
print(b.getstd())