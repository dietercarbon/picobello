#==========================================================================
#
# PB-02-7-10-Temperaturspeicherung.py
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
k=0

DateiT = open("Keller-Temperaturen.txt","w")
DateiT.write("Temperaturen im Keller\n")

# Endlos-Schleife starten
while True:
    k=k+1
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
    
    STRk=str(k)
    STRtemperatur = str(temperatur)[:5]
    SpeicherZeile=STRk+"  "+STRtemperatur+"\n"
    DateiT.write(SpeicherZeile)
    DateiT.flush()
    
    # 2 Sekunden warten
    sleep(2)
    
"""
Das vorliegende Micropython-Programm für den Raspberry Pi Pico liest
kontinuierlich die Temperatur mit einem Analog-Digital-Wandler (ADC)
aus dem eingebauten Temperatursensor aus und gibt die Temperatur in
Grad Celsius aus. Zusätzlich werden die Daten in einer Textdatei
gespeichert, um später eine Analyse durchführen zu können.

Zunächst werden die benötigten Bibliotheken "machine" für den ADC und
"utime" für die Zeitverzögerung beim Schleifendurchlauf importiert.

Anschließend wird der ADC4 initialisiert, welcher mit dem on-board
Temperatursensor verbunden ist. Die Bekannten Werte für den Temperatursensor
mit negativem Temperaturkoeffizienten werden angegeben. Hierbei ist zu
beachten, dass eine höhere Spannung niedrigere Temperaturen und eine
niedrigere Spannung höhere Temperaturen bedeutet. Der Umrechnungsfaktor
für die Spannungswerte wird berechnet.

Eine Schleife wird gestartet, in der der Temperatursensor ausgelesen wird.
Der ADC liest die analoge Spannung und wandelt diese in einen digitalen
Wert um. Der EinlesewertDigi geht von 0 - 65535, was dem Spannungsbereich
von 0 - 3,3 V entspricht. Anschließend wird dieser Wert in Spannung
umgerechnet. Da der Temperatursensor eine negative Temperaturabhängigkeit
aufweist, wird die Spannung in die Temperatur umgerechnet.

Die Temperatur wird in der Kommandozeile/Shell ausgegeben und in einer
Textdatei "Keller-Temperaturen.txt" gespeichert. Die Textdatei wird zu
Beginn der Schleife geöffnet und mit einem Header versehen, der den Inhalt
der Datei beschreibt. Jeder Messwert wird in einer neuen Zeile der Textdatei
gespeichert.

Abschließend wird die Schleife mit einer Verzögerung von 2 Sekunden durchlaufen.

Insgesamt handelt es sich um ein einfaches Micropython-Programm, das die
Temperatur aus dem on-board Temperatursensor des Raspberry Pi Pico ausliest,
in Grad Celsius umrechnet und in einer Textdatei speichert. Es ist einfach
zu verstehen und gut geeignet, um mit dem Raspberry Pi Pico und Micropython
zu experimentieren.
"""
