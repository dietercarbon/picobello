#==========================================================================
#
# PB-01-1-90-PrioMat.py
#
# (keine Bauteile)
#
#==========================================================================
#
#Bibliotheken importieren
import random
import utime

wort1 = ["Unsere Industrie ", "Deutschland ", "Unsere Gesellschaft ", "Unsere Politik ", "Die NATO ", "Die EU "]
wort2 = ["benötigt mehr ", "muss investieren in ", "muss aufholen bei ", "schläft auf dem Gebiet ", "hinkt hinterher bei ", "muss sich mehr engagieren bei ", "verschläft "]
wort3 = ["Robotik.", "KI.", "Digitalisierung.", "Autonomes Fahren.", "Drohneneinsatz.", "Vernetzung."]

while True:
    zufall1 = random.randint(0,len(wort1)-1)
    zufall2 = random.randint(0,len(wort2)-1)
    zufall3 = random.randint(0,len(wort3)-1)

    print()
#   print(zufall1,zufall2,zufall3)
    print(wort1[zufall1],wort2[zufall2],wort3[zufall3])
    
    utime.sleep(2)
    
"""
Das Programm verwendet die Programmiersprache MicroPython und ist für den
Raspberry Pi Pico Mikrocontroller ausgelegt. Das Ziel des Programms ist es,
zufällige Sätze aus einer Liste von Wörtern zu generieren und auf dem
Bildschirm auszugeben. Das Programm verwendet die Module "random" und "utime",
um Zufallszahlen zu erzeugen und eine Pause zwischen den Ausgaben der Sätze zu
erzeugen.

Der Code beginnt mit dem Import von zwei Modulen "random" und "utime". "random"
wird verwendet, um Zufallszahlen zu generieren, während "utime" für die Pause
zwischen den Ausgaben der Sätze verantwortlich ist.

Danach werden drei Listen definiert, "wort1", "wort2" und "wort3". Jede Liste
enthält eine Reihe von Wörtern oder Phrasen, die miteinander kombiniert werden,
um den Satz zu bilden. Die Wörter in jeder Liste sind durch Kommas getrennt und
werden in eckigen Klammern platziert.

In der while-Schleife wird ein endloser Schleifenblock ausgeführt. Innerhalb
der Schleife werden drei Zufallszahlen erzeugt, eine für jedes der drei Wörter
in den Listen. Die Zufallszahlen werden mit der Funktion "random.randint()"
erzeugt. Der erste Parameter ist 0 und der zweite Parameter ist die Länge der
Liste minus 1. Dies ist notwendig, da die Indizes in Python bei 0 beginnen und
die Länge der Liste um 1 größer ist als der höchste Index.

Anschließend wird der Satz aus den zufällig ausgewählten Wörtern zusammengesetzt
und auf dem Bildschirm ausgegeben. Die Funktion "print()" wird verwendet, um den
Satz auszugeben. Vor jedem Wort wird ein Leerzeichen eingefügt, damit der Satz
gut lesbar ist.

Schließlich wird eine Pause von 2 Sekunden zwischen den Ausgaben der Sätze
erzeugt, indem die Funktion "utime.sleep()" verwendet wird.

Zusammenfassend generiert das Programm zufällige Sätze aus vordefinierten
Wörtern und gibt sie auf dem Bildschirm aus, während es eine Pause zwischen
den Ausgaben einlegt. Es könnte als Ausgangspunkt für ein einfaches
Chatbot-Programm dienen oder als Teil eines größeren Projekts, bei dem
zufällige Sätze oder Wörter benötigt werden.


>>> %Run -c $EDITOR_CONTENT

Die NATO  verschläft  Drohneneinsatz.

Die NATO  muss aufholen bei  Robotik.

Deutschland  hinkt hinterher bei  Autonomes Fahren.

Deutschland  benötigt mehr  Autonomes Fahren.

Unsere Politik  hinkt hinterher bei  Autonomes Fahren.

Unsere Industrie  verschläft  Vernetzung.

Die EU  hinkt hinterher bei  Vernetzung.

Unsere Industrie  benötigt mehr  Robotik.


"""