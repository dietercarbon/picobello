#==========================================================================
#
# PB-02-7-20-Temperaturspeicherung einlesen.py
#
# (keine Bauteile)
#
#==========================================================================
#
DateiIn = open("Keller-Temperaturen.txt","r")

for i in range(11):
    print(DateiIn.readline())
    
DateiIn.close()

"""
Dieser Programmabschnitt öffnet die Datei "Keller-Temperaturen.txt" im
Lesemodus und gibt die ersten 11 Zeilen der Datei aus. Anschließend wird
die Datei geschlossen.

Kommentar zur Programmlogik:

Der Code liest eine Textdatei mit dem Namen "Keller-Temperaturen.txt" ein
und gibt die ersten 11 Zeilen dieser Datei in der Shell aus. Durch das
Öffnen der Datei im Lesemodus und das Verwenden der readline()-Methode
wird die Datei Zeile für Zeile durchgegangen und ausgegeben. Durch das
Schließen der Datei am Ende wird sichergestellt, dass keine Ressourcen
verschwendet werden.

Die for-Schleife wird 11-mal durchlaufen und jedes Mal wird die Methode
readline() aufgerufen, um eine Zeile aus der Datei zu lesen und in der
Shell auszugeben. Dadurch wird sichergestellt, dass nur die ersten 11 Zeilen
ausgegeben werden und nicht die gesamte Datei.

Der Code ist relativ einfach und leicht zu verstehen. Er zeigt, wie man
eine Datei in Python öffnet und Zeilen aus dieser Datei ausliest. Dies
kann nützlich sein, um Daten in einer Datei zu speichern und später zu
analysieren oder auszugeben.

Es ist jedoch zu beachten, dass dieser Code nur die ersten 11 Zeilen der
Datei ausgibt und nicht die gesamte Datei. Wenn man alle Zeilen aus der
Datei auslesen möchte, müsste man eine Schleife verwenden, die so oft
durchläuft, wie es Zeilen in der Datei gibt, oder man könnte die Methode
read() verwenden, um den gesamten Inhalt der Datei auf einmal auszulesen.

Insgesamt ist dies ein einfaches und nützliches Beispiel für den Umgang
mit Textdateien in Python.
"""