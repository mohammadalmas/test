import time
from Sensor import Sensor
class Heater:
    def __repr__(self):
        return f"{self.temp}"
    def __init__(self,temp=25):
        self.temp=temp
        self.sensor = Sensor()
    def on(self):
        return "Heater Is ON "
    def off(self):
        return "Heater Is OFF"
    def reach_request_temp(self):
        x = Sensor().temp_sensor()
        if x> self.temp:  #dama mohit mashin bishtar az damaye custom bashad bokhari khamosh shavad
            return self.off() , "Tempereture is top" , x
        else:
            print("Heater is on")
            print("dama mohit mashin is:",x)
            for i in range(x , self.temp+1):
                print(i,time.sleep(1))
            print("Heater is off")