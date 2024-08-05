#==========================================================================
#
# PB-02-1-11-LED extern und Summer try.py
#
# 1 LED, 1 Widerstand, 1 Summer
#
#==========================================================================
#
#Dieses Programm schaltet im Wechsel eine LED und einen Summer ein und aus.

# Laden der Bibliothek "machine" zur Nutzung der GPIO-Pins 14 und 15
import machine
# Laden der Bibliothek "utime" zur Nutzung von Pausen-Funktionen
import utime

# Definition der Variablen "externeLED" zur Vorbereitung einer Ausgabe auf GPIO-15
externeLED = machine.Pin(15, machine.Pin.OUT, value=0)
# Definition der Variablen "Piepsi" zur Vorbereitung einer Ausgabe auf GPIO-14
Piepsi = machine.Pin(14, machine.Pin.OUT)

try:
    # Start Endlos-Schleife
    while True:
        # Ein-Schalten der LED auf GPIO-15
        externeLED.value(1)
        # Pause von 0,9 Sekunden, also LED so lange an
        utime.sleep(0.9)
        # Aus-Schalten der LED auf GPIO-15
        externeLED.value(0)
        # Ein-Schalten des Summers auf GPIO-14
        Piepsi.value(1)
        # Pause von 0,1 Sekunden, also piepst so lange
        utime.sleep(0.1)
        # Aus-Schalten des Summers auf GPIO-14
        Piepsi.value(0)

except KeyboardInterrupt:
    print("\nStrg+C erkannt. Programm wird beendet.")
    # Hier kannst du optional Code für eine saubere Beendigung hinzufügen, falls benötigt.
    externeLED.value(0)
    Piepsi.value(0)
    print("sauber beendet")

finally:
    # Hier kannst du optional Code für die Endbereinigung hinzufügen, falls benötigt.
    pass


'''
Erklärung Zeilenweise:

    import machine: Importiert das machine-Modul, das Funktionen für die Steuerung von
    Hardware auf dem Raspberry Pi Pico bereitstellt.

    import utime: Importiert das utime-Modul, um Zeitverzögerungen zu ermöglichen.

    externeLED = machine.Pin(15, machine.Pin.OUT): Erstellt eine Variable externeLED
    und konfiguriert sie als Ausgang (OUT) für den GPIO-Pin 15, der mit einer
    externen LED verbunden ist.

    Piepsi = machine.Pin(14, machine.Pin.OUT): Erstellt eine Variable Piepsi und
    konfiguriert sie als Ausgang (OUT) für den GPIO-Pin 14, der mit einem Summer
    verbunden ist.

    try:: Beginnt einen Try-Block, in dem der Hauptprogrammcode ausgeführt wird.

    while True:: Startet eine Endlosschleife für den Hauptprogrammcode.

    externeLED.value(1): Schaltet die externe LED ein, indem der Ausgang
    auf 1 gesetzt wird.

    utime.sleep(0.9): Pausiert das Programm für 0,9 Sekunden (LED bleibt an).

    externeLED.value(0): Schaltet die externe LED aus, indem der Ausgang
    auf 0 gesetzt wird.

    Piepsi.value(1): Schaltet den Summer ein, indem der Ausgang auf 1 gesetzt wird.

    utime.sleep(0.1): Pausiert das Programm für 0,1 Sekunden (Summer bleibt an).

    Piepsi.value(0): Schaltet den Summer aus, indem der Ausgang auf 0 gesetzt wird.

    except KeyboardInterrupt:: Fängt die KeyboardInterrupt-Ausnahme ab,
    die ausgelöst wird, wenn Strg+C gedrückt wird.

    print("\nStrg+C erkannt. Programm wird beendet."): Gibt eine Abschlussmeldung aus.

    finally:: Beginnt einen Finally-Block, der unabhängig von Ausnahmen
    immer ausgeführt wird.

    pass: Platzhalter, um sicherzustellen, dass der finally-Block nicht leer ist.
    Hier könntest du optional Code für Endbereinigungen hinzufügen.
    
    '''