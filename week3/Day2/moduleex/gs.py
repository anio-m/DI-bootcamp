from dogcls import Dog 

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