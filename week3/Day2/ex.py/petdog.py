from ex import Dog
import random

class PetDog :
    def __init__(self, trained = False) :
        self.trained = trained
        
    
    def bark (self) :
        self.trained = True
        return self.trained
    
    def play (self, *args):
        print(f"{', '.join(args)} all play together")

dog5 = PetDog()
dog5.play('lessy', 'bob', 'junior')

dogi = ["does a barrel roll","stands on his back legs","shakes your hand","plays dead"]
def do_a_tick(self, trained) :
    if dog5 is trained :
        print (random(dogi))
    

do_a_tick()
