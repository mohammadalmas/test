from Heater import Heater
print ("Wellcome to here")
class Car:
    def __init__(self,model,color,year):
        self.model = model
        self.color = color
        self.year = year
        self.heater = Heater()
    def __repr__(self):
        return f"Model: {self.model} , Color:{self.color} , Year: {self.year}"
    def break_(self):
        return "This car is 'STOPING'"
    def turn_heater_on(self,temp):
        return self.heater.reach_request_temp()
a = Car("benz","Black",2020)
#print(a)
#print(a.turn_heater_on(10))
