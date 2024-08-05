#==========================================================================
#
# PB-02-1-20-Morsen.py
#
# 1 LED, 1 Widerstand, 1 Summer
#
#==========================================================================
#
import machine
import utime

externeLED = machine.Pin(15, machine.Pin.OUT, value=0)
Piepsi = machine.Pin(14, machine.Pin.OUT, value=0)

# https://en.wikipedia.org/wiki/Morse_code
# International Morse code is composed of five elements:
#    short mark, dot or dit: "dit duration" is one time unit long
#    long mark, dash or dah: three time units long
#    inter-element gap between the dits and dahs within a character: one dot duration or one unit long
#    short gap (between letters): three time units long
#    medium gap (between words): seven time units long

#    A 	.-
#    B 	-...
#    C 	-.-.
#    D 	-..
#    E 	.
#    F 	..-.
#    G 	--.
#    H 	....
#    I 	..
#    J 	.---
#    K 	-.-
#    L 	.-..
#    M 	--
#    N 	-.
#    O 	---
#    P 	.--.
#    Q 	--.-
#    R 	.-.
#    S 	...
#    T 	-
#    U 	..-
#    V 	...-
#    W 	.--
#    X 	-..-
#    Y 	-.--
#    Z 	--..
#    0 	-----
#    1 	.----
#    2 	..---
#    3 	...--
#    4 	....-
#    5 	.....
#    6 	-....
#    7 	--...
#    8 	---..
#    9 	----.

Faktor = 0.1
dit = 1 * Faktor
dah = 3 * Faktor
PauzwiZei = 1 * Faktor # Theorie: 1
PauzwiBu = 5 * Faktor  # Theorie: 3
PauzwiWo = 9 * Faktor  # Theorie: 7

Wort = input("Bitte Wort eingeben: ")

Länge = len(Wort)
print("Wortlänge: ",Länge)
Zähler = 0

while Zähler < Länge:
    print(Wort[Zähler])
    if (Wort[Zähler]) == "a":   #.-
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
    elif (Wort[Zähler]) == "b":   #-...
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    elif (Wort[Zähler]) == "c":   #-.-.
         #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
          #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz 
    elif (Wort[Zähler]) == "d":   #-..
         #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    elif (Wort[Zähler]) == "e":   #.
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    elif (Wort[Zähler]) == "f":   #..-.
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
         #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    elif (Wort[Zähler]) == "g":   #--.
         #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    elif (Wort[Zähler]) == "h":   #....
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    elif (Wort[Zähler]) == "i":   #..
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    elif (Wort[Zähler]) == "j":   #.---
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
         #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
         #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
         #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
    elif (Wort[Zähler]) == "k":   #-.-
         #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
    elif (Wort[Zähler]) == "l":   #.-..
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    elif (Wort[Zähler]) == "m":   #--
         #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
    elif (Wort[Zähler]) == "n":   #-.
         #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    elif (Wort[Zähler]) == "o":   #---
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
    elif (Wort[Zähler]) == "p":   #.--.
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    elif (Wort[Zähler]) == "q":   #--.-
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
         #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
    elif (Wort[Zähler]) == "r":   #.-.
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
         #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    elif (Wort[Zähler]) == "s":   #...
         #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
         #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
         #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    elif (Wort[Zähler]) == "t":   #-
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
    elif (Wort[Zähler]) == "u":   #..-
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
    elif (Wort[Zähler]) == "v":   #...-
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
    elif (Wort[Zähler]) == "w":   #.--
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
    elif (Wort[Zähler]) == "x":   #-..-
         #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
    elif (Wort[Zähler]) == "y":   #-.--
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
    elif (Wort[Zähler]) == "z":   #z: --..
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #lang
        Piepsi.value(1)
        utime.sleep(dah)
        Piepsi.value(0)
        #ende lang
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
        utime.sleep(PauzwiZei)
        #kurz
        Piepsi.value(1)
        utime.sleep(dit)
        Piepsi.value(0)
        #ende kurz
    else:
        utime.sleep(PauzwiWo)
    utime.sleep(PauzwiBu)
    Zähler = Zähler + 1
    
"""
Dieses Programm ist eine Implementation der Morsecode-Übersetzung auf einem
Raspberry Pi Pico Board mit der Programmiersprache MicroPython. Es gibt auch
eine kurze Theorie-Übersicht zum Morsecode.

Das Programm beginnt mit der Einrichtung der GPIO-Pins auf dem Raspberry Pi
Pico Board, die für die Ausgabe der Morsecode-Signale verwendet werden.
Pin 15 wird für die externe LED und Pin 14 für den Piezo-Summer konfiguriert.

Als Nächstes werden die unterschiedlichen Längen der Punkte, Striche und
Pausen des Morsecodes in Form von Faktoren definiert. Diese werden dann
multipliziert, um die eigentliche Dauer in Sekunden zu berechnen. Die
Berechnung erfolgt durch Multiplikation des Faktors mit der Anzahl der
Einheiten, die jedes Zeichen und jede Pause in Morsecode hat.

Der Benutzer wird aufgefordert, ein Wort einzugeben, das in Morsecode
umgewandelt werden soll. Der Eingabe-Text wird als eine Zeichenkette (string)
in der Variable Wort gespeichert.

Anschließend wird die Länge des Wortes mit der Python len() Funktion berechnet
und als Länge gespeichert. Die Variable Zähler wird auf 0 gesetzt und es wird
eine while-Schleife gestartet, die so lange ausgeführt wird, bis Zähler gleich
Länge ist.

Innerhalb der while-Schleife wird jedes Zeichen des eingegebenen Wortes
abgerufen und geprüft, ob es ein Zeichen des Morsecodes ist. Wenn es sich
um ein Zeichen des Morsecodes handelt, wird es durch die GPIO-Pins des
Raspberry Pi Pico Boards in ein Morsecode-Signal umgewandelt. Der Morsecode wird
durch das Ein- und Ausschalten des Piezo-Summers und der externen LED generiert.

Die Pausen zwischen den einzelnen Morsezeichen, Buchstaben und Wörtern werden
ebenfalls durch das Ein- und Ausschalten der GPIO-Pins generiert. Die Pausendauer
hängt von der Anzahl der Einheiten ab, die jeder Pause in Morsecode entsprechen.

Anschließend wird der Zähler um eins erhöht und die Schleife beginnt von vorne.
Das Programm endet, wenn der Zähler gleich der Länge des Wortes ist.

Zusammenfassend handelt es sich bei diesem Programm um eine Implementierung der
Morsecode-Übersetzung auf einem Raspberry Pi Pico Board mit der Programmiersprache
MicroPython. Das Programm nutzt die GPIO-Pins des Boards, um Morsecode-Signale
zu erzeugen, und kann vom Benutzer durch Eingabe eines beliebigen Wortes
aufgerufen werden. Es ist zu beachten, dass die Pausendauer im Code aufgrund
von Theorie-Erkenntnissen vom tatsächlichen Morsecode abweichen kann.
"""
    
    

