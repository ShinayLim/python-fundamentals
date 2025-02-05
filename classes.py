class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print("Eating...")
    def breathe(self):
        print("Breathing...")
        
class Dog(Animal):
    def sounds(self):
        print("Barking...")
        
class Cat(Animal):
    def sounds(self):
        print("Meowing...")
        
dog1 = Dog("Aw-aw")
dog1.eat()
dog1.sounds()

cat1 = Cat("Mingming")
cat1.eat()
cat1.sounds()