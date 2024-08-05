#==========================================================================
#
# PB-02-6-10-Temperaturmessung onboard.py
#
# (keine Bauteile)
#
#==========================================================================
#
# Bibliotheken laden
from machine import ADC
from utime import sleep

# Initialisierung des ADC4 (Analog-Digital-Converter, Kanal 4),
# welcher mit dem on-board Temperatursensor verbunden ist.
Temperatursensor = ADC(4)

# Bekannte Werte:
#Temperatursensor mit negativem Temperaturkoeffizienten, d.h.
#   höhere Spannung - > niedirigere Temperatur, und
#   niedrigere Spannung - > höhere Temperatur.
# 0,706 Volt entsprechen 27 Grad Celsius;
# + 1,721 mV = + 0,001721 V entspricht 1 Grad Celsius minus-Abweichung;
# - 1,721 mV = - 0,001721 V entspricht 1 Grad Celsius plus-Abweichung.

Umrechnungsfaktor = 3.3 / (65535)

# Endlos-Schleife starten
while True:
    # Temparatur-Sensor als Dezimalzahl lesen:
    # EinlesewertDigi geht von 0 - 65535
    EinlesewertDigi = Temperatursensor.read_u16()
    
    # EinlesewertDigi in Spannung umrechnen:
    # Spannung beträgt zwischen
    #    0 Volt bei EinlesewertDigi = 0, und
    #    3,3 Volt bei EinlesewertDigi = 65535.
    Spannung = EinlesewertDigi * Umrechnungsfaktor
    
    # Spannung in Temperatur umrechnen:
    # a. wenn Spannung um 0,001721 höher ist als 0.706, also 0,707721
    #    ist Klammer:  0,001721, und
    #    Bruch ergibt:  1, und
    #    Temperatur somit 27 - 1 = 26 Grad Celsius.
    # b. wenn Spannung um 0,001721 geringer ist als 0.706, also 0,704279
    #    ist Klammer:  - 0,001721, und
    #    Bruch ergibt:  - 1, und
    #    Temperatur somit 27 - -1 = 28 Grad Celsius.
    temperatur = 27 - (Spannung - 0.706) / 0.001721
    
    # Ausgabe in der Kommandozeile/Shell
    print("EinlesewertDigi: ", EinlesewertDigi)
    print("Spannung (V): ", Spannung)
    print("Temperatur (°C): ", temperatur)
    print()
    
    # 2 Sekunden warten
    sleep(2)
    
"""
Das Programm beginnt mit dem Laden von zwei Bibliotheken, machine und utime.
Die machine Bibliothek ist eine Sammlung von Modulen, die zur Steuerung von
Hardwarekomponenten des Raspberry Pi Pico verwendet werden können. Die utime
Bibliothek wird verwendet, um Zeitverzögerungen zu implementieren.

Der nächste Abschnitt initialisiert den ADC4, welcher mit dem on-board
Temperatursensor verbunden ist. Hier wird eine Instanz des ADCs mit der
Pin-Nummer 4 erstellt, die später verwendet wird, um die Temperatur zu messen.

Der folgende Abschnitt enthält einige Variablen, die zur Umrechnung der
Spannung in Temperatur verwendet werden. Der Kommentar beschreibt die
Details dieser Umrechnung.

In der Endlosschleife wird der Temperatursensor gelesen, indem der ADC-Wert
als Dezimalzahl gelesen und in eine Spannung umgerechnet wird. Die Spannung
wird dann in eine Temperatur umgerechnet und auf der Konsole ausgegeben.
Das Programm wartet dann 2 Sekunden, bevor es die Temperatur erneut misst
und die Schleife wiederholt.

Kommentar zum Programmverhalten:

Das Programm liest kontinuierlich die Temperatur von einem on-board
Temperatursensor aus und gibt sie auf der Konsole aus. Der ADC-Wert, der
den Temperatursensor liest, wird in eine Spannung umgewandelt und dann in
eine Temperatur umgerechnet. Die Temperatur wird dann in Grad Celsius
angezeigt. Das Programm wartet dann 2 Sekunden, bevor es die Temperatur
erneut misst und anzeigt.

Das Programm verwendet eine Schleife, die niemals endet, so dass es
unendlich Temperaturmessungen durchführt. Das Programm kann durch
Unterbrechung des Stromkreises oder durch Drücken der Reset-Taste
auf dem Raspberry Pi Pico gestoppt werden.

Zusammenfassend misst dieses Programm kontinuierlich die Temperatur
mithilfe des on-board Temperatursensors und gibt sie auf der Konsole aus.
Es ist ein einfaches Beispiel dafür, wie man einen Sensor ausliest und
die Daten auf der Konsole ausgibt.
"""

