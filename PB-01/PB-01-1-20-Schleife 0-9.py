#==========================================================================
#
# PB-01-1-20-Schleife 0-9.py
#
# (keine Bauteile)
#
#==========================================================================
#
print("Schleife startet!")

for Nummer in range(10):
    print("Schleifen-Nummer", Nummer)
print("Schleife beendet!")

"""
Das Programm gibt eine Startnachricht aus und startet dann eine Schleife,
die 10 Durchläufe durchführt. In jedem Durchlauf wird die aktuelle
Schleifennummer ausgegeben. Nachdem die Schleife beendet ist, wird eine
Endnachricht ausgegeben.

Die Schleife wird durch das Schlüsselwort for eingeleitet, gefolgt von
einer Variable (Nummer), die in jedem Durchlauf den Wert einer Zahl aus
dem Bereich range(10) annimmt. range(10) definiert eine Sequenz von Zahlen
von 0 bis 9, die der Schleife als Werte für die Variable Nummer dienen.

In jeder Schleife wird die aktuelle Schleifennummer zusammen mit dem
Text "Schleifen-Nummer" ausgegeben. Diese Ausgabe erfolgt mit der
Funktion print(). Am Ende der Schleife wird eine Endnachricht ausgegeben.


>>> %Run -c $EDITOR_CONTENT
Schleife startet!
Schleifen-Nummer 0
Schleifen-Nummer 1
Schleifen-Nummer 2
Schleifen-Nummer 3
Schleifen-Nummer 4
Schleifen-Nummer 5
Schleifen-Nummer 6
Schleifen-Nummer 7
Schleifen-Nummer 8
Schleifen-Nummer 9
Schleife beendet!
>>>

"""
