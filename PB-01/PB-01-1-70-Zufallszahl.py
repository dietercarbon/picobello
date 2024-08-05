#==========================================================================
#
# PB-01-1-70-Zufallszahl.py
#
# (keine Bauteile)
#
#==========================================================================
#
#Bibliotheken importieren
import utime
import random

while True:
    Zufallszahl = random.randint(0,10)
    print(Zufallszahl)
    utime.sleep(1)
    
"""
Das vorliegende MicroPython-Programm für den Raspberry Pi Pico importiert die
Module utime und random, um eine zufällige Zahl zu generieren und diese dann
alle 1 Sekunde auszugeben.

Innerhalb der while-Schleife wird eine Zufallszahl zwischen 0 und 10 mithilfe
der Funktion random.randint() aus dem Modul random erzeugt und in der Variablen
Zufallszahl gespeichert.

Die print()-Funktion wird dann verwendet, um die aktuelle Zufallszahl auf der
Konsole auszugeben. Anschließend wird das Programm mithilfe der Funktion
utime.sleep() für eine Sekunde pausiert, bevor die Schleife erneut durchlaufen
wird.

Dieser Vorgang wird kontinuierlich ausgeführt, solange das Programm läuft, da
die Bedingung while True stets erfüllt ist.

Zusammenfassend erzeugt dieses Programm eine zufällige Zahl zwischen 0 und 10
und gibt sie alle 1 Sekunde aus, bis das Programm gestoppt wird.

Nun zur verbalen Erklärung des Codes:

Das Programm importiert zuerst die Module utime und random. utime stellt
Funktionen zur Zeitmessung und -verwaltung bereit, während random Funktionen
zum Generieren von Zufallszahlen enthält.

Innerhalb der while-Schleife wird eine Zufallszahl zwischen 0 und 10 mithilfe
der Funktion random.randint() aus dem Modul random generiert. Diese Zufallszahl
wird dann mithilfe der print()-Funktion auf der Konsole ausgegeben.

Um sicherzustellen, dass die Ausgabe verlangsamt wird, damit sie vom Benutzer
besser wahrgenommen werden kann, wird das Programm mithilfe der Funktion
utime.sleep() für eine Sekunde pausiert. Anschließend beginnt die Schleife
erneut mit der Generierung einer neuen Zufallszahl.

Dieser Vorgang wird unendlich oft wiederholt, solange das Programm läuft,
da die Bedingung while True immer erfüllt ist.

Dieses Programm ist ein gutes Beispiel für die Verwendung von Schleifen und
Zeitfunktionen in MicroPython, um kontinuierlich Zufallszahlen auszugeben.
Es zeigt auch die Verwendung von Modulen in MicroPython und die Funktion
random.randint(), um Zufallszahlen zu generieren.


>>> %Run -c $EDITOR_CONTENT
10
6
6
0
3
6
6


"""