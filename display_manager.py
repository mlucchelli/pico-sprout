from picographics import PicoGraphics, DISPLAY_LCD_240X240, PEN_P8, PEN_RGB332
from math import pi, radians
import jpegdec

class DisplayManager:
    def __init__(self, pen_color):
        self.display = PicoGraphics(display=DISPLAY_LCD_240X240, pen_type=PEN_RGB332, rotate=90 )
        self.display.set_backlight(0.9)
        self.display.set_font("bitmap8")
        self.jpeg_decoder = jpegdec.JPEG(self.display)
        self.pen_color = pen_color
        self.max_lines = 10
        self.lines = []
        self.yellow_pen = self.display.create_pen(255,255,0)
        self.white_pen = self.display.create_pen(255,255,255)
        self.green_pen = self.display.create_pen(0,255,0)
        self.aqua_green_pen = self.display.create_pen(0, 255, 255)
        self.blue_pen = self.display.create_pen(0,170,228)
        self.pink_pen = self.display.create_pen(255, 192, 203)
        

    def print_image(self, filename):
        self.jpeg_decoder.open_file(filename)
        self.jpeg_decoder.decode(2, 110, jpegdec.JPEG_SCALE_FULL, dither=False)
        
    def print_display(self, output_text, x, y, wordwrap, scale, font_color, font, bg_color):
        self.display.set_pen(font_color)
        self.display.text(output_text, x, y, wordwrap, scale)
        self.display.set_pen(0)

    def set_pen(self, color):
       self.display.set_pen(color)

    def log(self, text):
        self.lines.append(text)

        if len(self.lines) > self.max_lines:
            self.lines.pop(0)

        self.display.clear()

        y = 0
        for line in self.lines:
            self.display.text(str(line), 0, y, scale=2)
            y += 16

        self.display.update()
        
    def draw_line(self, x1, y1, x2, y2, color):
        self.display.set_pen(color)
        self.display.line(x1, y1, x2, y2)
    
    def draw_progress_bar(self, x, y, width, height, fill_percentage, custom_color=None):
        fill_percentage = max(0, min(fill_percentage, 100))  # Ensure fill_percentage is between 0 and 100
        fill_width = int(width * fill_percentage / 100)

        # Set pen color
        if custom_color is not None:
            self.display.set_pen(custom_color)
        else:
            self.display.set_pen(0)  # Default color

        # Draw the filled portion based on the fill percentage using the rectangle method
        self.display.rectangle(x, y, fill_width, height)

        self.display.update()

        # Reset pen color to default
        self.display.set_pen(0)
        
    def draw_v_progress_bar(self, x, y, width, height, fill_percentage, custom_color=None):
        fill_percentage = max(0, min(fill_percentage, 100))  # Ensure fill_percentage is between 0 and 100
        fill_height = int(height * fill_percentage / 100)

        # Set pen color
        if custom_color is not None:
            self.display.set_pen(custom_color)
        else:
            self.display.set_pen(0)  # Default color

        # Draw the filled portion based on the fill percentage using the rectangle method
        
        self.display.rectangle(x, y, width, fill_height)
        print("height: ", fill_height)
        self.display.update()

        # Reset pen color to default
        self.display.set_pen(0)
        