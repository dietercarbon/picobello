#==========================================================================
#
# PB-02-8-10-Temperaturspeicherung try.py
#
# (keine Bauteile)
#
#==========================================================================
#
# Bibliotheken laden
from machine import ADC
from utime import sleep

Temperatursensor = ADC(4)

Umrechnungsfaktor = 3.3 / (65535)
k=0
VersNr = 1

try:
    Dateiname="Keller-Temperaturen"+str(VersNr)+".txt"
    DateiT = open(Dateiname,"r")
    
    while True:
        VersNr = VersNr + 1
        try:
            Dateiname="Keller-Temperaturen"+str(VersNr)+".txt"
            DateiT = open(Dateiname,"r")
        except OSError as e:
            print(f"Fehler beim Öffnen der Datei: {e}")
            break
      
    Dateiname="Keller-Temperaturen"+str(VersNr)+".txt"
    DateiT = open(Dateiname,"w")
    
except OSError as e:
    print(f"Fehler beim Öffnen der Datei: {e}")
    '''
Die Fehlermeldung "[Errno 2] ENOENT" steht für einen "No such file or directory"-
Fehler in Unix-ähnlichen Betriebssystemen. In diesem Kontext bedeutet
ENOENT "Error Number 2" und gibt an, dass die angegebene Datei oder das
angegebene Verzeichnis nicht gefunden wurde.
'''
    DateiT = open(Dateiname,"w")

while True:
    k=k+1

    EinlesewertDigi = Temperatursensor.read_u16()
    Spannung = EinlesewertDigi * Umrechnungsfaktor
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
Das Programm läuft in einer Endlosschleife und führt folgende Schritte aus:
   1. Inkrementiert die Zählvariable 'k'.
   2. Liest den Analog-Digital-Wert des Temperatursensors ein.
   3. Berechnet die Spannung und Temperatur basierend auf dem eingelesenen Wert.
   4. Gibt die eingelesenen Werte sowie die Temperatur in der Kommandozeile aus.
   5. Schreibt die gemessene Temperatur zusammen mit der Zählvariablen in die Textdatei.
   6. Schläft für 2 Sekunden, bevor der nächste Schleifendurchlauf beginnt.

Es ist wichtig zu beachten, dass das Programm in einer Endlosschleife ausgeführt wird,
sodass es kontinuierlich Temperaturmessungen durchführt und die Daten in die Datei schreibt.

Zum Beenden des Programms muss es manuell unterbrochen werden.

die 1. try-Schleife:

    Der erste try-Block versucht, eine Datei mit dem Namen "Keller-Temperaturen" plus
    der aktuellen VersNr (Versionsnummer) und der Dateiendung ".txt" im Lesemodus
    zu öffnen (open(Dateiname, "r")). Dabei wird der Variablen Dateiname der Name der Datei zugewiesen.

    Innerhalb dieses try-Blocks befindet sich eine while-Schleife, die solange läuft,
    bis eine nicht existierende Datei gefunden wird. In jedem Schleifendurchlauf wird
    die Versionsnummer (VersNr) erhöht, und es wird versucht, die nächste Datei im
    Lesemodus zu öffnen. Falls eine OSError-Ausnahme auftritt, wird dies erkannt,
    eine entsprechende Fehlermeldung ausgegeben, und die Schleife wird durch break beendet.

    Nachdem die Schleife durchlaufen wurde, wird versucht, die Datei im Schreibmodus
    zu öffnen (open(Dateiname, "w")). Falls dabei ein Fehler auftritt,
    wird er erneut behandelt, und es wird versucht, die Datei im Schreibmodus zu öffnen.

die 2. try-Schleife:

    Diese except-Anweisung behandelt den Fall, wenn beim Öffnen der Datei ein OSError
    auftritt, z.B. wenn die Datei nicht gefunden wird. In diesem Fall wird eine
    entsprechende Fehlermeldung ausgegeben.

    Zusätzlich wird eine Kommentarzeile ausgegeben, die erklärt, dass die
    Fehlermeldung "[Errno 2] ENOENT" auf einen Fehler hinweist, dass die
    angegebene Datei oder das Verzeichnis nicht gefunden wurde.

    Danach wird versucht, die Datei im Schreibmodus zu öffnen, um sie
    zu erstellen, falls sie nicht existiert.

"""