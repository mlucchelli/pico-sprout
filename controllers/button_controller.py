import utime

class ButtonController:
    def __init__(self, pin, long_press_duration, debounce_time=20):
        self.pin = pin
        self.long_press_duration = long_press_duration
        self.debounce_time = debounce_time
        self.state_on = "on"
        self.state_off = "off"
        self.state_long_pressed = "long_pressed"
        self.state_released = "released"
        self.last_change_time = 0
        self.prev_pin_state = self.pin.value()
        self.long_press_detected = False
        self.subscribers = []

    def add_subscribers(self, subscribers):
        self.subscribers = subscribers

    def notify_subscribers(self, event):
        for subscriber in self.subscribers:
            print(type(subscriber).__name__)
            print(subscriber.is_active())
            if(subscriber.is_active()):
                subscriber.notify(event)

    def read(self):
        current_time = utime.ticks_ms()
        pin_state = self.pin.value()
        # Check if enough time has passed since the last pin state change
        if utime.ticks_diff(current_time, self.last_change_time) > self.debounce_time:
            # Check if there has been a pin state change
            if pin_state != self.prev_pin_state:
                self.last_change_time = current_time
                self.prev_pin_state = pin_state

                # Wait for additional time before reading the pin state
                utime.sleep_ms(self.debounce_time)

                # Read the pin state again
                pin_state = self.pin.value()
                if pin_state == 1:
                    long_press_start_time = utime.ticks_ms()
                    while self.pin.value() == 1:
                        if utime.ticks_diff(utime.ticks_ms(), long_press_start_time) >= self.long_press_duration:
                            print("button state: long_pressed")
                            self.long_press_detected = True
                            self.notify_subscribers(self.state_long_pressed)
                            return self.state_long_pressed
                    # If no long press is detected, set the flag to False
                    self.long_press_detected = False
                    print("button state: on")
                    self.notify_subscribers(self.state_on)
                    return self.state_on
                else:
                    # If the button is released and no long press was detected, return 'released'
                    if not self.long_press_detected:
                        print("button state: released")
                        self.notify_subscribers(self.state_released)
                        return self.state_released 
        return self.prev_pin_state
    
