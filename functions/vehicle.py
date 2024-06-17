#INHERITANCE

class Vehicle:
    def __init__(self, make, color):
        self.make = make
        self.color = color

    def accelerate(self):
        print("Acceleration starts")

    def hoot(self):
        print("honk honk")     

class Bus(Vehicle):
    def __init__(self, make, color, passengers):
        super().__init__(make, color)
        self.passengers = passengers

    def start_boarding(self):
        print("Thr bus is boarding")

class Lorry(Vehicle):
    def __init__(self, make, color,max_hold):
        super().__init__(make, color)  
        self.max_hold = max_hold

    def unload(self):
        print("unloading")              

        