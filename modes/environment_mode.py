import utime
from .mode import Mode

class EnvironmentMode(Mode):
    def __init__(self, display_manager, environment_sensor, potentiometer, button, interval_minutes ):
        super().__init__(display_manager, interval_minutes)
        self.environment_sensor = environment_sensor
        self.button = button
        self.display_manager = display_manager
        self.potentiometer = potentiometer
        self.edit_minutes_max = 60
        self.current_edit_minutes = 0

    def draw_main(self):
        print("draw main")
        self.display_manager.print_display('Temperature', 40, 15, 1, 3, self.display_manager.yellow_pen, "", 255)
        self.display_manager.print_display(str(round(self.environment_sensor.bme_temperature, 1))+'c', 40, 60, 10, 7, 255, "", 255)
                
        self.display_manager.draw_line(20,130,220, 130, self.display_manager.white_pen)
               
        self.display_manager.print_display('Humidity', 60, 145, 1, 3, self.display_manager.blue_pen, "", 255)
        self.display_manager.print_display(str(round(self.environment_sensor.bme_humidity, 1))+'%', 40, 185, 10, 7, 255, "", 255)


    def draw_edit(self):
        self.display_manager.print_display(str(round(self.current_edit_minutes, 1)), 5, 30, 1, 25, self.display_manager.white_pen, "", 255)

    def draw_screen(self):
        if self.edit_mode():
            self.draw_edit()
        else:
            self.draw_main()

    
    def notify(self, event):
        if(event == self.button.state_long_pressed):
            if not self.edit_mode():
                self.mode = 1
                print("edit mode")
        elif(event == self.button.state_released):
            if self.edit_mode():
                self.interval_minutes = self.current_edit_minutes
                self.exit_edit()

    
    def update_mode(self):   
        if(self.edit_mode):
            self.current_edit_minutes = self.potentiometer.read(self.edit_minutes_max)
            
    def exit_edit(self):
        self.mode = 0
        self.edit_step = 0
        self.recently_edited = True
        print("return to main")
        self.draw()

