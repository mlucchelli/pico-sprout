import utime
from .mode import Mode

class PumpMode(Mode):
    def __init__(self, display_manager, pump, potentiometer, button, interval_minutes):
        super().__init__(display_manager, interval_minutes)
        self.pump1 = pump
        self.button = button
        self.display_manager = display_manager
        self.mode = 0
        self.potentiometer = potentiometer
        self.edit_minutes_max = 21
        self.current_edit_minutes = 0
        self.edit_step = 0

    def draw_main(self):
        self.display_manager.draw_line(5,5,235, 5, self.display_manager.white_pen)
        color = self.display_manager.white_pen
        if(self.pump1.pump_state == self.pump1.state_on):
            color = self.display_manager.aqua_green_pen
        
        self.display_manager.print_display('Pump: ' + self.pump1.pump_state, 10, 25, 240, 5, color, "", 255)
                            
        self.display_manager.draw_line(5,75,235, 75, self.display_manager.white_pen)
        if self.pump1.last_pump_turned_on !=0:
            self.display_manager.print_display("Last: "+ self.utime_to_time_string(self.pump1.last_pump_turned_on), 10, 95, 235, 3, self.display_manager.white_pen, "", 255)
        
        else:
            self.display_manager.print_display("Last: never", 10, 95, 235, 3, self.display_manager.white_pen, "", 255)
        self.display_manager.print_display("Next: " + self.utime_to_future_time_string(self.calculate_remaining_time(self.pump1.last_pump_turned_on, self.pump1.watering_frequency * 3600000)), 10, 150, 235, 3, self.display_manager.white_pen, "", 255)

        progress_percentage = 0
        color = self.display_manager.white_pen
        if(self.pump1.pump_state == self.pump1.state_on):

            remaining_time = self.calculate_remaining_time(self.pump1.last_pump_turned_on, self.pump1.watering_duration_minutes * 60000)
            progress_percentage = (1 - remaining_time / (self.pump1.watering_duration_minutes * 60000)) * 100
            color = self.display_manager.aqua_green_pen

        else:
            remaining_time = self.calculate_remaining_time(self.pump1.last_pump_turned_on, self.pump1.watering_frequency * 3600000)
            progress_percentage = (1 - remaining_time / (self.pump1.watering_frequency * 3600000)) * 100
        self.display_manager.draw_progress_bar(x=10, y=205, width=200, height=10, fill_percentage=progress_percentage, custom_color=color)
        

    def draw_edit(self):

        if(self.edit_step == 1):
            self.display_manager.print_display('Irrigation', 55, 15, 1, 3, self.display_manager.yellow_pen, "", 255)
            self.display_manager.print_display(str(round(self.current_edit_minutes, 1)), 15, 50, 1, 25, self.display_manager.white_pen, "", 255)
        elif(self.edit_step == 2):
            self.display_manager.print_display('Frequency', 55, 15, 1, 3, self.display_manager.yellow_pen, "", 255)
            self.display_manager.print_display(str(round(self.current_edit_minutes, 1)), 15, 50, 1, 25, self.display_manager.white_pen, "", 255)

    def draw_screen(self):
        if self.edit_mode():
            self.draw_edit()
        else:
            self.draw_main()

    def update_mode(self):
        if(self.edit_mode):
            self.current_edit_minutes = self.potentiometer.read(self.edit_minutes_max)
    
    def exit_edit(self):
        self.mode = 0
        self.edit_step = 0
        self.recently_edited = True
        print("return to main")
        self.draw()

    def notify(self, event):
        if(event == self.button.state_long_pressed):
            if not self.edit_mode():
                self.mode = 1
                self.edit_step = 1
                self.edit_minutes_max = 21
                print("edit mode")
        elif(event == self.button.state_released):
            if self.edit_mode():
                if(self.edit_step == 1):
                    self.pump1.watering_duration_minutes = self.current_edit_minutes
                    self.edit_minutes_max = 8
                    self.edit_step  = 2
                else:
                    self.pump1.watering_frequency = self.current_edit_minutes * 24
                    self.exit_edit()
            else:
                self.pump1.toggle_pump() 

        
    def utime_to_time_string(self, utime_tick):
        current_time = utime.ticks_ms()
        difference_ms = current_time - utime_tick
        seconds = difference_ms // 1000
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        time_difference_str = "{}D {}H {}m".format(days, hours, minutes)

        return time_difference_str

    def calculate_remaining_time(self, utime_tick, watering_frequency):
        current_time = utime.ticks_ms()
        elapsed_ms = (current_time - utime_tick)

        time_remaining = (watering_frequency) - elapsed_ms
        return int(time_remaining)  # Convertir horas a ms

    def utime_to_future_time_string(self, utime_tick):
        seconds = utime_tick // 1000
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        time_difference_str = "{}D {}H {}M".format(days, hours, minutes)

        return time_difference_str
        
    