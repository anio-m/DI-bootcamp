from gs import GermanShepard
# import the class GermanShepard from the gs file
from dogcls import Dog

my_dog = GermanShepard(100, "Rex")
my_dog.jump()
my_dog.bark() # woof 10 times
print(my_dog.__dict__)

my_other_dog = Dog("Lola", "chihuaua", "white", 1)
my_other_dog.run()
my_other_dog.bark() # woof 10 times
print(my_other_dog.__dict__)

# other types of import 

# import gs

# my_dog = gs.GermanShepard(100, "Rex")
# my_dog.jump()
# my_dog.bark() # woof 10 times
# print(my_dog.__dict__)
