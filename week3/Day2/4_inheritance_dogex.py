class Dog :

    def __init__(self, name, type, color, velocity):
        self.name = name
        self.type = type
        self.color = color
        self.velocity = velocity

    def bark (self) :
        print("WOUF WOUF")
    
    def change_color (self, new_color) :
        self.color = new_color
    
    def run (self) :
        print(f"I run at {self.velocity} km per hour")

# inheritance
# GermanShepard inherits from the Dog class
# it can use all the methods and attributes from the dog class
# child of the Dog class
class GermanShepard(Dog) :
    
    def __init__(self, IQ, name) :
        super().__init__(name, "GermanShepard", "Brown", 12)
        self.IQ = IQ

    # only for german shepard
    # can only run before jumping
    def jump (self) :
        super().run() #calling the method of the parent
        print("I jump high")
    
    # same function name, means overriding
    def bark (self) :
        print("WOOF"*10)


my_dog = GermanShepard(100, "Rex")
my_dog.jump()
my_dog.bark() # woof 10 times
print(my_dog.__dict__)

# print(dir(my_dog))

# lea_dog = Dog("Spock", "chihuahua", "white", 1)
# lea_dog.jump()