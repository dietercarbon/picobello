#==========================================================================
#
# PB-02-3-10-Adventskalender.py
#
# 5 LEDs, 5 Widerstände
#
#==========================================================================
#
import utime
import machine

LED1_1 = machine.Pin(7, machine.Pin.OUT, value=0)
LED2_2 = machine.Pin(9, machine.Pin.OUT, value=0)
LED3_4 = machine.Pin(11, machine.Pin.OUT, value=0)
LED4_8 = machine.Pin(13, machine.Pin.OUT, value=0)
LED5_16 = machine.Pin(15, machine.Pin.OUT, value=0)

LED1_1.value(0)
LED2_2.value(0)
LED3_4.value(0)
LED4_8.value(0)
LED5_16.value(0)


while True:
    dez=1
    while dez<25:
        print("dez-Wert in Zeile 18 :",dez)
#        dez_str=input("der wievielte Dezember ist heute? ")
#        dez = int(dez_str)
        LED1_1.value(0)
        LED2_2.value(0)
        LED3_4.value(0)
        LED4_8.value(0)
        LED5_16.value(0)
        if dez==1:
            print(dez,". Dezember")
            LED1_1.value(1)
            LED2_2.value(0)
            LED3_4.value(0)
            LED4_8.value(0)
            LED5_16.value(0)
        elif dez==2:
            print(dez,". Dezember")
            LED2_2.value(1)
        elif dez==3:
            print(dez,". Dezember")
            LED1_1.value(1)
            LED2_2.value(1)
        elif dez==4:
            print(dez,". Dezember")
            LED3_4.value(1)
        elif dez==5:
            print(dez,". Dezember")
            LED1_1.value(1)
            LED3_4.value(1)
        elif dez==6:
            print(dez,". Dezember")
            LED2_2.value(1)
            LED3_4.value(1)
        elif dez==7:
            print(dez,". Dezember")
            LED1_1.value(1)
            LED2_2.value(1)
            LED3_4.value(1)
        elif dez==8:
            print(dez,". Dezember")
            LED4_8.value(1)
        elif dez==9:
            print(dez,". Dezember")
            LED1_1.value(1)
            LED4_8.value(1)
        elif dez==10:
            print(dez,". Dezember")
            LED2_2.value(1)
            LED4_8.value(1)
        elif dez==11:
            print(dez,". Dezember")
            LED1_1.value(1)
            LED2_2.value(1)
            LED4_8.value(1)
        elif dez==12:
            print(dez,". Dezember")
            LED3_4.value(1)
            LED4_8.value(1)
        elif dez==13:
            print(dez,". Dezember")
            LED1_1.value(1)
            LED3_4.value(1)
            LED4_8.value(1)
        elif dez==14:
            print(dez,". Dezember")
            LED2_2.value(1)
            LED3_4.value(1)
            LED4_8.value(1)
        elif dez==15:
            print(dez,". Dezember")
            LED1_1.value(1)
            LED2_2.value(1)
            LED3_4.value(1)
            LED4_8.value(1)
        elif dez==16:
            print(dez,". Dezember")
            LED5_16.value(1)
        elif dez==17:
            print(dez,". Dezember")
            LED1_1.value(1)
            LED5_16.value(1)
        elif dez==18:
            print(dez,". Dezember")
            LED2_2.value(1)
            LED5_16.value(1)
        elif dez==19:
            print(dez,". Dezember")
            LED1_1.value(1)
            LED2_2.value(1)
            LED5_16.value(1)
        elif dez==20:
            print(dez,". Dezember")
            LED3_4.value(1)
            LED5_16.value(1)
        elif dez==21:
            print(dez,". Dezember")
            LED1_1.value(1)
            LED3_4.value(1)
            LED5_16.value(1)
        elif dez==22:
            print(dez,". Dezember")
            LED2_2.value(1)
            LED3_4.value(1)
            LED5_16.value(1)
        elif dez==23:
            print(dez,". Dezember")
            LED1_1.value(1)
            LED2_2.value(1)
            LED3_4.value(1)
            LED5_16.value(1)
        else:
            print(dez,". Dezember")
            LED1_1.value(0)
            LED2_2.value(0)
            LED3_4.value(0)
            LED4_8.value(1)
            LED5_16.value(1)
        print("nach if Schleife")
        utime.sleep(1)
        dez=dez+1
        
"""
Das Programm verwendet die Programmiersprache MicroPython, die für eingebettete
Systeme optimiert ist, und läuft auf einem Raspberry Pi Pico. Es dient dazu,
fünf LEDs zu steuern und je nach Wert einer Variablen namens "dez"
unterschiedliche Kombinationen von LEDs zu aktivieren.

Zu Beginn des Programms werden fünf GPIO-Pins als Ausgangspins initialisiert
und anschließend auf 0 gesetzt, um sicherzustellen, dass alle LEDs ausgeschaltet
sind.

Anschließend beginnt eine Endlosschleife. Innerhalb dieser Schleife wird die
Variable "dez" auf 1 initialisiert und dann durch eine While-Schleife gezählt,
bis sie 24 erreicht hat. Dies bedeutet, dass die Schleife insgesamt 24 Mal
durchlaufen wird.

Innerhalb der Schleife wird zuerst überprüft, welcher Wert "dez" hat. Abhängig
vom Wert werden verschiedene Kombinationen von LEDs aktiviert oder deaktiviert.
Wenn "dez" zum Beispiel den Wert 1 hat, wird nur die erste LED aktiviert,
während bei einem Wert von 7 alle fünf LEDs eingeschaltet werden.

Zwischen jedem Durchlauf der While-Schleife wird eine Pause von einer Sekunde
eingefügt, um sicherzustellen, dass der Code nicht zu schnell ausgeführt wird.
"""