#==========================================================================
#
# PB-01-1-40-Endlos-Schleife.py
#
# (keine Bauteile)
#
#==========================================================================
#
#Bibliotheken importieren
import utime

print("Schleife starten!")

while True:
    print("Schleife läuft!")
    utime.sleep(1)
print("Schleife beendet!")

"""
Das Programm beginnt mit dem Importieren des "utime"-Moduls, das Funktionen
zur Zeitmessung und Verzögerung enthält. Dann wird eine Meldung ausgegeben,
um anzuzeigen, dass die Schleife gestartet wird. Die Schleife selbst ist eine
Endlosschleife, die immer wieder ausgeführt wird, bis sie von außen
unterbrochen wird. Innerhalb der Schleife wird eine Meldung ausgegeben,
um anzuzeigen, dass die Schleife läuft. Der Code wird für eine Sekunde
pausiert, um die Schleife nicht zu schnell durchlaufen zu lassen.

Es gibt keine Bedingung innerhalb der Schleife, um sie zu beenden, daher
wird der letzte print-Befehl ("Schleife beendet!") nie ausgeführt werden.
Dieses Programm könnte in einer Schleife verwendet werden, die ständig auf
Eingaben oder Ereignisse wartet, wie z.B. in einem IoT-Anwendungsfall, bei
dem ein Gerät ständig auf eine Verbindung zum Netzwerk wartet.


>>> %Run -c $EDITOR_CONTENT
Schleife starten!
Schleife läuft!
Schleife läuft!
Schleife läuft!
Schleife läuft!
Schleife läuft!

"""
