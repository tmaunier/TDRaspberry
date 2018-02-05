from gpiozero import LED, Buzzer
from time import sleep
from RPLCD.gpio import CharLCD
from RPi import GPIO

led = LED(4)
buzzer = Buzzer(17)
lcd = CharLCD(pin_rs=15, pin_rw=None,  pin_e=16, pins_data=[21,22,23,24], numbering_mode=GPIO.BCM, cols=16, rows=2, dotsize=8,charmap='A02', auto_linebreaks=True)

dicoMorse = {"A":(1,2), "B":(2,1,1,1), "C":(2,1,2,1), "D":(2,1,1), "E":(1,0), "F":(1,1,2,1),"G":(2,2,1),
             "H":(1,1,1,1), "I":(1,1), "J":(1,2,2,2), "K":(2,1,2), "L":(1,2,1,1), "M":(2,2), "N":(2,1),
             "O":(2,2,2), "P":(1,2,2,1), "Q":(2,2,1,2), "R":(1,2,1), "S":(1,1,1), "T":(2,0), "U":(1,1,2),
             "V":(1,1,1,2), "W":(1,2,2), "X":(2,1,1,2), "Y":(2,1,2,2), "Z":(2,2,1,1)}

# def display_letter(letter):
#     for item in dicoMorse[letter]:
#         print(".", end="") if item == 1 else print("_", end="")
#     print(" ", end="")

def emit_signal(letter, current_word):
    for item in dicoMorse[letter]:
        lcd.write_string(current_word)
        led.on()
        buzzer.on()
        sleep(0.1) if item == 1 else sleep(0.3)
        led.off()
        buzzer.off()
        lcd.clear()
    sleep(0.3)

def main():
    current_word = ""
    lcd.clear()
    text = raw_input("Text : ").upper()

    for letter in text:
        if letter == " ":
            sleep(0.7)
            current_word += " "
            # print(end="  ")
            continue
        current_word += letter
        emit_signal(letter, current_word)
        # display_letter(letter)



if __name__ == "__main__":
    main()