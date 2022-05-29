from posixpath import split
import Adafruit_CharLCD as LCD

class Display:
    def __init__(self) -> None:
        # Raspberry Pi pin configuration:
        self.lcd_rs        = 25
        self.lcd_en        = 24
        self.lcd_d4        = 23
        self.lcd_d5        = 17
        self.lcd_d6        = 18
        self.lcd_d7        = 22
        self.lcd_backlight = 1

        # Define LCD column and row size for 16x2 LCD.
        self.lcd_columns = 16
        self.lcd_rows    = 2

    def show(self, text):
        # Initialize the LCD using the pins above.
        lcd = LCD.Adafruit_CharLCD(self.lcd_rs, self.lcd_en, self.lcd_d4, self.lcd_d5, self.lcd_d6, self.lcd_d7,
                                self.lcd_columns, self.lcd_rows, self.lcd_backlight)

        lcd.message(text)