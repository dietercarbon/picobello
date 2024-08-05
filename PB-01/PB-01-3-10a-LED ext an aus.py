#==========================================================================
#
# PB-01-3-10-LED ext an aus.py
#
# 1 LED, 1 Widerstand
#
#==========================================================================
#
#Bibliotheken importieren
import machine
import utime

externeLED = machine.Pin(15, machine.Pin.OUT)

while True:
    externeLED.value(1)
    print("an")
    utime.sleep(1)
    externeLED.value(0)
    print("aus")
    utime.sleep(1)

"""
Das Programm verwendet die Micropython-Bibliothek für die Ansteuerung von Pins
auf dem Raspberry Pi Pico. Es initialisiert Pin 15 als Ausgang und erstellt ein
Objekt für diesen Pin.

Das Programm enthält eine Schleife, die unendlich läuft. In jeder Iteration der
Schleife wird Pin 15 für 0,9 Sekunden auf 1 gesetzt und dann für 0,1 Sekunden
auf 0 gesetzt. Dies erzeugt einen blinkenden Effekt auf der externen LED, die
an Pin 15 angeschlossen ist.

Der Wert 1 auf Pin 15 aktiviert den LED und 0 deaktiviert ihn. Die Funktion
utime.sleep() wird verwendet, um eine Pause zwischen den Änderungen des
Pin-Status zu erzeugen.

Insgesamt ist das Programm sehr einfach und führt eine grundlegende Steuerung
einer externen LED durch. Es könnte als Basis für weitere Projekte und
Experimente mit der GPIO-Schnittstelle des Raspberry Pi Pico dienen.
"""