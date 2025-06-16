# class dog
class Dog:
    def __init__(self, name, age): # __init__() method is a special method that Python runs automatically whenever we create a new instance based on the Dog class.
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name.title()} is sitting on the bench:")

    def roll_over(self):
        print(f"{self.name.title()} is rolling over the plastic bag:")
my_dog = Dog('hero', 10)
print(f"my dog name is {my_dog.name}.")
print(f"my dog age is {my_dog.age}.")
my_dog.sit() # When Python reads my_dog.sit(), it looks for the method sit() in the class Dog and runs that code. 
my_dog.roll_over()

# creating multiple instances
my_dog = Dog('hola', 5)
your_dog = Dog('susam',6)
print(f"\nmy dog's name is {my_dog.name.title()}.")
my_dog.sit()
my_dog.roll_over()

print(f"\nyour dog name is {your_dog.name.title()}.")
your_dog.sit()
your_dog.roll_over()