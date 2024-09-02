import time
from pimoroni_i2c import PimoroniI2C
from breakout_potentiometer import BreakoutPotentiometer

class PotentiometerController:
    def __init__(self, i2c_pins, brightness=1.0, direction=BreakoutPotentiometer.DIRECTION_CW):
        self.i2c = PimoroniI2C(**i2c_pins)
        self.pot = BreakoutPotentiometer(self.i2c)
        self.pot.set_brightness(brightness)
        self.pot.set_direction(direction)
        self.rgb_led = None

    def map_potentiometer_value(self, value, pot_min, pot_max, num_elements):
        index = int((value - pot_min) / (pot_max - pot_min) * (num_elements - 1))
        index = max(0, min(index, num_elements - 1))
        return index

    def read(self, num_elements):
        val = self.pot.read()
        index = self.map_potentiometer_value(val, 0.0, 0.99, num_elements)
        del val
        return index

    def set_rgb_color(self, color):
        self.pot.set_led(color["r"], color["g"], color["b"])
