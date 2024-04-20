import random
class Sensor:
    def __repr__(self):
        return f"Tempereture Sensor : {self.temp_sensor()}"
    def temp_sensor(self):
        return random.randint(5,20)
