import utime

class Mode:
    def __init__(self, display_manager, interval_minutes):
        self.mode = 0
        self.state_active = "active"
        self.state_inactive = "inactive"
        self.state = self.state_inactive
        self.edit_minutes_max = 60
        self.current_edit_minutes = 0
        self.update_frequency = 10
        self.recently_edited = False
        self.display_manager = display_manager
        self.interval_minutes = interval_minutes
        self.last_action_time = utime.ticks_ms() - (self.interval_minutes * 60000)
        self.refreshed = False
    
    def notify(self, event):
        print("not implemented")

    def is_active(self):
        return self.state == self.state_active
    
    def draw_screen(self):
         print("not implemented")

    def draw(self):
        print("drawing mode")
        self.display_manager.display.clear()
        self.draw_screen()
        self.display_manager.display.update()

    def update_mode():
        print("not implemented")


    def update(self):
        elapsed_minutes = (utime.ticks_ms() - self.last_action_time) / 60000
        if(self.edit_mode()):
            self.update_mode()
        if elapsed_minutes >= self.interval_minutes:
            self.last_action_time = utime.ticks_ms()
            self.refreshed = True
        

    def is_refreshed(self):
        if self.refreshed == False:
            return self.refreshed
        else:
            self.refreshed = False
            return not self.refreshed

    def edit_mode(self):
        if self.mode == 0:
            return False
        elif self.mode == 1:
            return True
    
    
