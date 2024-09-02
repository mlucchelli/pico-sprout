import utime
import time
import network
import urequests as requests
import machine
from machine import Pin, I2C, ADC
from display_manager import DisplayManager
from controllers.potentiometer_controller import PotentiometerController
from controllers.soil_sensor_controller import SoilSensorController
from controllers.environment_sensor_controller import EnvironmentSensorController
from controllers.button_controller import ButtonController
from controllers.pump_controller import PumpController

from modes.environment_mode import EnvironmentMode
from modes.soil_mode import SoilMode
from modes.pump_mode import PumpMode
from modes.core_mode import CoreMode
from modes.button_mode import ButtonMode


# end of import

potentiometer_enabled = True

# status led
led_pin = Pin("LED", Pin.OUT)

# display
display_manager = DisplayManager(255)

#environment sensor
environment_sensor = EnvironmentSensorController(sda_pin=2, scl_pin=3)

# soil sensors
soil1 = SoilSensorController(ADC(Pin(28, Pin.IN)))
soil2 = SoilSensorController(ADC(Pin(27, Pin.IN)))

# potentiometer input
if(potentiometer_enabled):
    PINS_BREAKOUT_GARDEN = {"sda": 12, "scl": 13}
    pot_control = PotentiometerController(PINS_BREAKOUT_GARDEN)
else:
    pot_control = None

# button input
button = ButtonController(Pin(1, Pin.IN,Pin.PULL_DOWN), long_press_duration=3000, debounce_time=50)
button_toggle = ButtonController(Pin(0, Pin.IN,Pin.PULL_DOWN), long_press_duration=3000, debounce_time=50)

# pump controller
pump_pin = Pin(15, Pin.OUT)
watering_duration_minutes = 1
watering_frequency = 24
min_moisture = 10
pump1 = PumpController(pump_pin, watering_duration_minutes, watering_frequency, soil1, soil2, min_moisture)


# modes
# each mode is in charge to monitor or manage specific resources
interval_minutes =  1
interval_minutes_pump = 0.05
environment_mode = EnvironmentMode(display_manager, environment_sensor, pot_control, button, interval_minutes)
soil_mode = SoilMode(display_manager, soil1, soil2, pot_control, button, interval_minutes)
pump_mode = PumpMode(display_manager, pump1, pot_control, button, interval_minutes_pump)

modes = []
modes.append(environment_mode)
modes.append(soil_mode)
modes.append(pump_mode)
core_mode = CoreMode(display_manager, led_pin, soil1, soil2, environment_sensor, pot_control, button, interval_minutes, modes)
button.add_subscribers(modes)

button_mode = ButtonMode(display_manager, interval_minutes, button_toggle, len(modes))
button_toggle.add_subscribers([button_mode])


display_mode = 0

# end of variable init
led_pin.value(0)

#
# Main
#
display_manager.print_display('Init', 10, 10, 10, 5, 255, "", 255)

time.sleep(1)

pump1.pump_switch(1, pump1.switch_auto)
soil1.read()
soil2.read()


while True:
    button.read()
    button_toggle.read()
    core_mode.update()
    modes[display_mode].update()
    if(potentiometer_enabled):
        display_value = pot_control.read(len(modes))
    else:
        display_value = button_mode.current_display
        
    if((display_mode != display_value) or core_mode.is_refreshed() or modes[display_mode].is_refreshed() or modes[display_mode].edit_mode()):
        if(not modes[display_mode].edit_mode()):
            modes[display_mode].state = modes[display_mode].state_inactive
            display_mode = display_value
            modes[display_mode].state = modes[display_mode].state_active
            core_mode.read_sensors()
        modes[display_mode].draw()
    pump1.run_cycle()

