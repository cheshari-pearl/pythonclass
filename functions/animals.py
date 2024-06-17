#POLYMORPHISM
class Animal:
    def move(self):
        pass

    def make_sound(self):
        pass
class Bird(Animal):
    def move(self):
        print("flying") 

    def make_sound(self):
        print("Chirp")

class Cat(Animal):
    def move(self):
        print("walking") 

    def make_sound(self):
        print("Meow")   

class Fish(Animal):
    def move(self):
        print("swimming") 

    def make_sound(self):
        print("Bop")                       