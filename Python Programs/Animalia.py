# Define parent class animalia  
class Animalia:  
      
    # define construcors for parent animalia class  
    def __init__(self):  
        self.Legs = 4  
        self.adomestic = True  
        self.atail = True  
        self.amammals = True  
  
    # define mammal class as child class  
    def aMammal(self):  
        if self.amammals:   
            print("The given animal is a mammal type .")  
  
    # define domestic class as child class  
    def aDomestic(self):  
        if self.adomestic:  
            print("The given animal is a domestic animal type.")  
# define dog class    
class Dog(Animalia):  
    def __init__(self):  
        super().__init__() # using super() function to access class methods  
  
    def isMammal(self):  
        super().aMammal() # using mammal class  
  
# define cat class  
class Cat(Animalia):  
    def __init__(self):  
        super().__init__()  
  
    def isMammal(self):  
        super().aDomestic() # using domestic class  
  
# define horse class  
class Horse(Animalia):  
    def __init__(self):  
        super().__init__()  
  
    def TailandLegs(self): # using tail and legs class  
        if self.atail and self.Legs == 4:  
            print("The given animal has four legs and a tail")  
  
# Taking the driver's code for defined classes  
Tommy = Dog()  
Tommy.aMammal()  
Tom = Cat()  
Tom.aDomestic()  
Burno = Horse()  
Burno.TailandLegs()  
