# 🌟 Exercise 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'    

cat1 = Bengal('Max', 2)
cat2 = Chartreux('bobi', 2)
cat3 = Siamese('joker', 2)


all_cats = [cat1, cat2, cat3]

sara_pets = Pets(all_cats)

sara_pets.walk()


# 🌟 Exercise 2 

class Dog :
    def __init__(self, name, age, weight) :
        self.name = name
        self.age = age
        self.weight = weight

    def bark (self) :
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight/self.age*10

    def fight(self, other_dog) :
      if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
          return self.name
      else :
          return other_dog.name
      

dog1 = Dog("bob", 6, 60)
dog2 = Dog("joker", 8, 90)
dog3 = Dog("tariner", 1, 35) 
print (dog1.fight(dog2))  
    



# 🌟 Exercise 3