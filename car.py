class Car(object):
    def __init__(self, colour, company, speed, model):
        self.colour = colour
        self.company = company
        self.speed = speed
        self.model = model

    def accelerate(self):
        print("Accelerating! Hold on tight!")

    def brake(self):
        print("Stopped! You can get off!")
    
audi = Car("red","audi",100,"a9")

print(audi.accelerate())