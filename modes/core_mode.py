import utime
from .mode import Mode


class CoreMode(Mode):
    def __init__(self, display_manager, led_pin, soil_sensor1, soil_sensor2, environment_sensor, potentiometer, button, interval_minutes, modes):
        super().__init__(display_manager, interval_minutes)
        self.display_manager = display_manager
        self.led_pin = led_pin
        self.soil_sensor1 = soil_sensor1
        self.soil_sensor2 = soil_sensor2
        self.environment_sensor = environment_sensor
        self.button = button
        self.potentiometer = potentiometer
        self.modes = modes

    def update_mode(self):
        self.read_sensors()


    def read_sensors(self):
        self.led_pin.value(1)
        print("updating environment sensor")
        self.environment_sensor.read()
            
        print("updating soil sensor 1")
        self.soil_sensor1.read()

        print("updating soil sensor 2")
        self.soil_sensor2.read()
        self.led_pin.value(0)

