#==========================================================================
#
# PB-01-1-30-Schleife 1-10.py
#
# (keine Bauteile)
#
#==========================================================================
#
print("Schleife startet!")

for Nummer in range(1,11):
    print("Schleifen-Nummer", Nummer)
print("Schleife beendet!")

"""
Das Programm besteht aus einem For-Loop, der von 1 bis 10 zählt und bei jedem
Durchlauf eine Nachricht ausgibt. Zunächst wird die Nachricht "Schleife startet!"
ausgegeben, dann beginnt die Schleife mit der Variable "Nummer", die von
1 bis 10 zählt. Bei jedem Durchlauf der Schleife wird die Nachricht
"Schleifen-Nummer" zusammen mit der aktuellen Nummer ausgegeben.
Nachdem alle Schleifendurchläufe abgeschlossen sind, wird die Nachricht
"Schleife beendet!" ausgegeben.

Insgesamt ist dies ein sehr einfaches Programm, das die grundlegenden
Konzepte von Schleifen und Ausgaben demonstriert. Es ist nützlich, um zu
verstehen, wie Schleifen in Python funktionieren und wie Variablen in einer
Schleife verwendet werden können.

Eine Anmerkung ist jedoch, dass die Schleife mit 1 beginnt, da die
Range-Funktion standardmäßig bei 0 beginnt, es sei denn, es wird ein anderer
Startwert angegeben. Dies kann in einigen Fällen zu Verwirrung führen, wenn
man erwartet, dass die Schleife bei 1 beginnt. In diesem Fall ist es jedoch
kein Problem, da der Code korrekt funktioniert und die Schleife bei 1 beginnt
und bei 10 endet.


>>> %Run -c $EDITOR_CONTENT
Schleife startet!
Schleifen-Nummer 1
Schleifen-Nummer 2
Schleifen-Nummer 3
Schleifen-Nummer 4
Schleifen-Nummer 5
Schleifen-Nummer 6
Schleifen-Nummer 7
Schleifen-Nummer 8
Schleifen-Nummer 9
Schleifen-Nummer 10
Schleife beendet!
>>>

"""
