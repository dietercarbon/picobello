#==========================================================================
#
# PB-02-1-10-LED extern und Summer.py
#
# 1 LED, 1 Widerstand, 1 Summer
#
#==========================================================================
#
#Dieses Programm schaltet im Wechsel eine LED und einen Summer ein und aus.

#Laden der Bibliothek "machine" zur Nutzung der GPIO-Pins 14 und 15
import machine
#Laden der Bibliothek "utime" zur Nutzung von Pausen-Funktionen
import utime

#Definition der Variablen "externeLED" zur Vorbereitung einer Ausgabe auf GPIO-15
externeLED = machine.Pin(15, machine.Pin.OUT, value=0)
#Definition der Variablen "Piepsi" zur Vorbereitung einer Ausgabe auf GPIO-14
Piepsi = machine.Pin(14, machine.Pin.OUT, value=0)

#Start Endlos-Schleife
while True:
    #Ein-Schalten der LED auf GPIO-15
    externeLED.value(1)
    #Pause von ... Sekunden, also LED so lange an
    utime.sleep(0.9)
    #Aus-Schalten der LED auf GPIO-15
    externeLED.value(0)
    #Ein-Schalten des Summers auf GPIO-14
    Piepsi.value(1)
    #Pause von ... Sekunden, also piepst so lange
    utime.sleep(0.1)
    #Aus-Schalten des Summers auf GPIO-14
    Piepsi.value(0)
    #Weiter mit Zeile 15
    
"""
Das Programm schaltet abwechselnd eine LED und einen Summer ein und aus.
Es verwendet die Bibliotheken "machine" und "utime" zur Steuerung der GPIO-Pins
und zum Einfügen von Pausen.

In den ersten beiden Zeilen des Programms werden die Bibliotheken "machine" und
"utime" geladen. In den Zeilen 5 und 6 werden die Variablen "externeLED" und
"Piepsi" definiert, um die GPIO-Pins 15 und 14 vorzubereiten. Der Pin 15 wird
für die LED verwendet und der Pin 14 für den Summer.

In der Schleife "while True" beginnt der Programmablauf bei Zeile 10. Zunächst
wird die LED eingeschaltet, indem der Wert der Variable "externeLED" auf 1 gesetzt
wird. Danach wird eine Pause von 0,9 Sekunden eingelegt, um die LED für diese Zeit
eingeschaltet zu lassen. Anschließend wird die LED wieder ausgeschaltet, indem der
Wert der Variable "externeLED" auf 0 gesetzt wird.

Danach wird der Summer eingeschaltet, indem der Wert der Variable "Piepsi" auf 1
gesetzt wird. Eine kurze Pause von 0,1 Sekunden wird eingelegt, um den Summer für
diese Zeit ertönen zu lassen. Danach wird der Wert der Variable "Piepsi" auf 0
gesetzt, um den Summer wieder auszuschalten.

Die Schleife wiederholt sich endlos und es wird immer abwechselnd die LED und
der Summer ein- und ausgeschaltet.

Insgesamt handelt es sich um ein sehr einfaches Programm, das die Grundlagen
der Verwendung von GPIO-Pins auf dem Raspberry Pi Pico demonstriert.
"""
