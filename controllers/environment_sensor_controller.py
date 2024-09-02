from bme680 import *
from breakout_bme68x import BreakoutBME68X
from pimoroni_i2c import PimoroniI2C
class EnvironmentSensorController:
    def __init__(self, sda_pin, scl_pin):
        PINS_PICO_EXPLORER = {"sda": sda_pin, "scl": scl_pin}
        i2c = PimoroniI2C(**PINS_PICO_EXPLORER)
        self.sensor = BreakoutBME68X(i2c)
        self.bme_temperature = 0
        self.pressure = 0
        self.bme_humidity = 0
        self.gas_resistance = 0
        self.status = 0
        self.gas_index = 0
        self.meas_index = 0
 
    def read(self):
        self.bme_temperature, self.pressure, self.bme_humidity, self.gas_resistance, self.status, self.gas_index, self.meas_index = self.sensor.read()
