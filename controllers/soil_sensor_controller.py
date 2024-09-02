class SoilSensorController:
    def __init__(self, pin):
        self.sensor = pin
        self.min_moisture = 0
        self.max_moisture = 65535
        self.moisture = 0

    def read(self):
        self.moisture = int((self.max_moisture-self.sensor.read_u16())*100/(self.max_moisture-self.min_moisture))
        return self.moisture
