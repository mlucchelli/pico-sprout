import utime
from .mode import Mode

class SoilMode(Mode):
    def __init__(self, display_manager, soil_sensor1, soil_sensor2, potentiometer, button, interval_minutes ):
        super().__init__(display_manager, interval_minutes)
        self.soil_sensor1 = soil_sensor1
        self.soil_sensor2 = soil_sensor2
        self.button = button
        self.display_manager = display_manager
        self.mode = 0
        self.potentiometer = potentiometer
        self.edit_minutes_max = 60
        self.current_edit_minutes = 0

    def draw_main(self):
        self.display_manager.print_display('Sensor A', 10, 35, 235, 3, self.display_manager.aqua_green_pen, "", 255)
        self.display_manager.print_display(str(self.soil_sensor1.moisture)+'%', 145, 40, 10, 6, 255, "", 255)
        self.display_manager.draw_progress_bar(x=10, y=95, width=200, height=10, fill_percentage=self.soil_sensor1.moisture, custom_color=self.display_manager.aqua_green_pen)
                
        self.display_manager.print_display('Sensor B', 10, 145, 235, 3, self.display_manager.pink_pen, "", 255)
        self.display_manager.print_display(str(self.soil_sensor2.moisture)+'%', 145, 145, 10, 6, 255, "", 255)
        self.display_manager.draw_progress_bar(x=10, y=205, width=200, height=10, fill_percentage=self.soil_sensor2.moisture, custom_color=self.display_manager.pink_pen)


    def draw_edit(self):
        self.display_manager.print_display(str(round(self.current_edit_minutes, 1)), 30, 30, 1, 25, self.display_manager.white_pen, "", 255)

    def draw_screen(self):
        if self.edit_mode():
            self.draw_edit()
        else:
            self.draw_main()

    def update_mode(self):
        if(self.edit_mode):
            self.current_edit_minutes = self.potentiometer.read(self.edit_minutes_max)
