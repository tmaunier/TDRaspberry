from RPLCD.gpio import CharLCD
from RPi import GPIO
import time

lcd = CharLCD(pin_rs=15, pin_rw=None,  pin_e=16, pins_data=[21,22,23,24], numbering_mode=GPIO.BCM, cols=16, rows=2, dotsize=8,charmap='A02', auto_linebreaks=True)

lcd.write_string("Allo \r\n le monde !")
time.sleep(5)
lcd.clear()
lcd.write_string("Hello \r\n world !")
