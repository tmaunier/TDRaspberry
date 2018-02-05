from gpiozero import LED, buzzer
from time import sleep

led = LED(4)
buzzer = buzzer.Buzzer(17)

dicoMorse = {"A":(1,2), "B":(2,1,1,1), "C":(2,1,2,1), "D":(2,1,1), "E":(1,0), "F":(1,1,2,1),"G":(2,2,1),
             "H":(1,1,1,1), "I":(1,1), "J":(1,2,2,2), "K":(2,1,2), "L":(1,2,1,1), "M":(2,2), "N":(2,1),
             "O":(2,2,2), "P":(1,2,2,1), "Q":(2,2,1,2), "R":(1,2,1), "S":(1,1,1), "T":(2,0), "U":(1,1,2),
             "V":(1,1,1,2), "W":(1,2,2), "X":(2,1,1,2), "Y":(2,1,2,2), "Z":(2,2,1,1)}

# def display_letter(letter):
#     for item in dicoMorse[letter]:
#         print(".", end="") if item == 1 else print("_", end="")
#     print(" ", end="")

def emit_signal(letter):
    for item in dicoMorse[letter]:
        led.on()
        buzzer.on()
        sleep(0.1) if item == 1 else sleep(0.3)
        led.off()
        buzzer.off()
    sleep(0.3)

def main():
    text = input("Text : ").upper()

    for letter in text:
        if letter == " ":
            sleep(0.7)
            # print(end="  ")
            continue
        emit_signal(letter)
        # display_letter(letter)



if __name__ == "__main__":
    main()