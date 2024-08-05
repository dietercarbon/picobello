#==========================================================================
#
# PB-01-2-10-LED_auf_Pico an aus.py
#
# (keine Bauteile)
#
#==========================================================================
#
#Bibliotheken importieren
import machine
import utime

LED_auf_Pico = machine.Pin(25, machine.Pin.OUT)
#LED_auf_Pico = machine.Pin("LED", machine.Pin.OUT)

while True:
    LED_auf_Pico.value(1)
    utime.sleep(0.1)
    LED_auf_Pico.value(0)
    utime.sleep(0.7)
    
"""
Das Programm steuert die LED an Pin 25 des Raspberry Pi Pico. Zunächst werden
die benötigten Module importiert: machine für den Zugriff auf Hardware-Pins
und utime für Verzögerungen. Die LED wird als Ausgangspins initialisiert,
indem machine.Pin(25, machine.Pin.OUT) aufgerufen wird.

In der while-Schleife wird die LED im Wechsel ein- und ausgeschaltet. Dazu
wird LED_auf_Pico.value(1) aufgerufen, um die LED einzuschalten. Anschließend
wartet das Programm 0,1 Sekunden, indem utime.sleep(0.1) aufgerufen wird.
Danach wird die LED mit LED_auf_Pico.value(0) ausgeschaltet, gefolgt von
einer Wartezeit von 0,7 Sekunden mit utime.sleep(0.7).

Das Programm führt diese Schleife kontinuierlich aus, bis es manuell
gestoppt wird.

Zusammenfassend lässt sich sagen, dass dieses Programm die LED auf dem
Raspberry Pi Pico steuert, indem sie abwechselnd ein- und ausgeschaltet
wird. Es nutzt dabei die Bibliotheken machine und utime, um auf die Hardware
zuzugreifen und Verzögerungen zu erzeugen.


>>> %Run -c $EDITOR_CONTENT



"""