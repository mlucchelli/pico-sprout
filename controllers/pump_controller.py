import utime
class PumpController:
    def __init__(self, pump_pin, watering_duration_minutes, watering_frequency, soil_sensor1, soil_sensor2, moisture):
        self.pump_pin = pump_pin
        self.watering_duration_minutes = watering_duration_minutes
        self.watering_frequency = watering_frequency 
        self.watering_frequency_minutes =  self.watering_frequency * 60
        self.last_pump_turned_on = 0
        self.state_off = "off"
        self.state_on = "on"
        self.pump_state = self.state_off
        self.soil_sensor1 = soil_sensor1
        self.soil_sensor2 = soil_sensor2
        self.min_moisture = moisture
        self.switch_manual = "manual"
        self.switch_auto = "auto"
        self.type_of_switch = self.switch_manual

    def pump_switch(self, state, type_of_switch):
        print("old pump state:", self.pump_state)
        print("new pump state:", state)   
        self.pump_pin.value(state)


    def run_cycle(self):
        current_time = utime.ticks_ms()
        elapsed_minutes = (current_time - self.last_pump_turned_on) / 60000

        if self.pump_state == self.state_off:
            if elapsed_minutes >= self.watering_frequency_minutes or self.last_pump_turned_on == 0:
                self.pump_state = self.state_on
                self.pump_switch(0, self.switch_auto)
                self.last_pump_turned_on = current_time
                print("Pump was turn on", current_time)

        elif self.pump_state == self.state_on:
            if elapsed_minutes >= self.watering_duration_minutes:
                self.pump_state = self.state_off
                self.pump_switch(1, self.switch_auto)
                print("Pump was turn off", current_time)
    
    def plants_need_water(self):
        return (self.soil_sensor1.moisture < 10) & (self.soil_sensor2.moisture < 10)
    
    def pump_is_on(self):
        return self.pump_state == self.state_on

    def toggle_pump(self):
        if self.pump_is_on():
            self.pump_switch(1, self.switch_manual)
            self.pump_state = self.state_off
        else:
            current_time = utime.ticks_ms()
            self.pump_switch(0, self.switch_manual)
            self.pump_state = self.state_on
            self.last_pump_turned_on = current_time

    def is_auto_switch(self):
        return self.type_of_switch == self.switch_auto

        