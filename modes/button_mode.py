import utime
from .mode import Mode

class ButtonMode(Mode):
    def __init__(self, display_manager, interval_minutes, button_toggle, modes_count):
        super().__init__(display_manager, interval_minutes)
        self.initial_display = 0
        self.count_display = modes_count
        self.current_display =  self.initial_display
        self.state = self.state_active
        self.button = button_toggle


    
    def notify(self, event):
        print(event)
        if(event == self.button.state_released):
            print(self.count_display)
            if(self.current_display < self.count_display -1):
                self.current_display = self.current_display + 1
            else:
                self.current_display = 0

