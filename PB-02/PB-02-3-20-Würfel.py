#==========================================================================
#
# PB-02-3-20-Würfel.py
#
# 5 LEDs, 5 Widerstände
#
#==========================================================================
#
import utime
import machine
import random

LED1_1 = machine.Pin(7, machine.Pin.OUT, value=0)
LED2_2 = machine.Pin(9, machine.Pin.OUT, value=0)
LED3_4 = machine.Pin(11, machine.Pin.OUT, value=0)
LED4_8 = machine.Pin(13, machine.Pin.OUT, value=0)
LED5_16 = machine.Pin(15, machine.Pin.OUT, value=0)

Start = 1
Ende = 6

while True:
    Augen = random.randint(Start,Ende)
    
    print("gewürfelt: ",Augen)

    LED1_1.value(0)
    LED2_2.value(0)
    LED3_4.value(0)

    if Augen==1:
        LED1_1.value(1)
    elif Augen==2:
        LED2_2.value(1)
    elif Augen==3:
        LED1_1.value(1)
        LED2_2.value(1)
    elif Augen==4:
        LED3_4.value(1)
    elif Augen==5:
        LED1_1.value(1)
        LED3_4.value(1)
    elif Augen==6:
        LED2_2.value(1)
        LED3_4.value(1)

    utime.sleep(1)

"""
Das Programm verwendet die Programmiersprache Micropython und ist für den
Raspberry Pi Pico Mikrocontroller geschrieben. Es erzeugt eine Simulation
des Würfelwerfens auf einer LED-Matrix mit fünf LEDs.

In den ersten Zeilen des Codes werden die Pin-Nummern für jede der fünf
LEDs als Konstanten definiert und dann jeweils als Ausgang konfiguriert.

Die nächsten Zeilen setzen alle LEDs auf den Zustand "Aus" (LED aus) und
dienen somit als Initialisierung.

Der Hauptteil des Codes befindet sich in einer Endlosschleife (while True:).
Innerhalb dieser Schleife wird eine Zufallszahl zwischen 1 und 6 generiert,
die die Augenzahl des simulierten Würfels darstellt. Dies wird durch die
Verwendung der random.randint Funktion erreicht.

Die aktuelle Augenzahl wird auf der Konsole ausgegeben
(print("gewürfelt: ",Augen)).

Danach werden alle LEDs auf "Aus" gesetzt (LED1_1.value(0), usw.), um
sicherzustellen, dass keine alte Anzeige des vorherigen Würfelergebnisses
verbleibt.

Anschließend werden die LEDs entsprechend der gewürfelten Augenzahl
eingeschaltet, indem die entsprechenden Pins auf den Zustand "Ein" (LED an)
gesetzt werden. Dies wird mit einer Kombination von if, elif und else
Anweisungen erreicht.

Schließlich wird das Programm für eine Sekunde pausiert (utime.sleep(1)),
um das Ergebnis für den Benutzer sichtbar zu machen, bevor die Schleife
erneut durchlaufen wird.

Zusammenfassend simuliert das Programm das Würfeln eines sechsseitigen
Würfels und zeigt das Ergebnis auf einer LED-Matrix mit fünf LEDs an.

Insgesamt scheint der Code klar und leicht verständlich zu sein. Es
verwendet auch eine gute Menge an Kommentaren, um den Zweck und die
Funktionsweise der einzelnen Zeilen des Codes zu erklären. Es wäre
jedoch schön, wenn es eine Kommentarzeile geben würde, die das Ziel
des gesamten Programms zusammenfasst.
"""
