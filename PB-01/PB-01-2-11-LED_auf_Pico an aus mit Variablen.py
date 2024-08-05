#==========================================================================
#
# PB-01-2-11-LED_auf_Pico an aus mit Variablen.py
#
# (keine Bauteile)
#
#==========================================================================
#
#Bibliotheken importieren
import machine
import utime

LED_auf_Pico = machine.Pin(25, machine.Pin.OUT)
LED_auf_Pico = machine.Pin("LED", machine.Pin.OUT)

an=0.1
aus=1

while True:
    LED_auf_Pico.value(1)
    utime.sleep(an)
    LED_auf_Pico.value(0)
    utime.sleep(aus)

"""
Das Programm steuert eine LED, die an Pin 25 des Raspberry Pi Pico
angeschlossen ist. Es verwendet die MicroPython-Module "machine" und "utime".
Das "machine" -Modul wird verwendet, um den GPIO-Pin 25 als Ausgang zu
konfigurieren. Das "utime" -Modul wird verwendet, um Zeitverzögerungen
zwischen dem Ein- und Ausschalten der LED zu erzeugen.

In der ersten Zeile des Codes wird das "machine" -Modul importiert.
Dieses Modul enthält Funktionen zur Steuerung der Hardware auf dem
Raspberry Pi Pico.

In der zweiten Zeile wird das "utime" -Modul importiert, das Funktionen
zur Zeitmessung und Zeitverzögerung bereitstellt.

In der dritten Zeile wird die Variable "LED_auf_Pico" erstellt und
Pin 25 als Ausgang konfiguriert. Der zweite Parameter "machine.Pin.OUT"
gibt an, dass der Pin als Ausgang konfiguriert wird.

In der nächsten Zeile werden zwei Variablen "an" und "aus" mit den Werten
0,1 und 1 definiert. Diese Werte werden verwendet, um die Verzögerungen
zwischen dem Ein- und Ausschalten der LED einzustellen.

In der Schleife wird zuerst die LED auf Pin 25 eingeschaltet, indem der
Wert des GPIO-Pins auf 1 gesetzt wird. Dann wird mit der "utime.sleep()"
-Funktion eine Pause von "an" Sekunden eingelegt. Anschließend wird die
LED ausgeschaltet, indem der Wert des GPIO-Pins auf 0 gesetzt wird.
Eine Pause von "aus" Sekunden wird mit "utime.sleep()" eingelegt,
bevor die Schleife erneut ausgeführt wird.

Zusammenfassend lässt sich sagen, dass das Programm die LED auf Pin 25
des Raspberry Pi Pico in einem bestimmten Muster ein- und ausschaltet,
wobei die Verzögerungen zwischen den Zuständen durch die Variablen "an"
und "aus" gesteuert werden. Das Programm wird in einer Endlosschleife
ausgeführt, sodass die LED kontinuierlich blinkt.


>>> %Run -c $EDITOR_CONTENT

"""