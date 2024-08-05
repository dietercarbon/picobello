#==========================================================================
#
# PB-01-4-10-Typ-Bestimmung.py
#
# (keine Bauteile)
#
#==========================================================================
#
#Bibliotheken importieren
import machine
import utime

NullEins = input("0 = ich probiere LED  und   1 = fehlertolerant: ")

#print("Z 15: NullEins = ",NullEins)

if NullEins == "1":
    #print("Z 18")
    try:
        LED_auf_Pico = machine.Pin("LED", machine.Pin.OUT)
    except Exception as e:
        LED_auf_Pico = machine.Pin(25, machine.Pin.OUT)
        print("ist Pico")
    else:
        print("ist Pico W")
        LED_auf_Pico = machine.Pin("LED", machine.Pin.OUT)
elif NullEins == "0":
    #print("Z 28")
    LED_auf_Pico = machine.Pin("LED", machine.Pin.OUT)
    
print("blink - blink - blink - blink - blink")

while True:
    LED_auf_Pico.value(1)
    utime.sleep(0.1)
    LED_auf_Pico.value(0)
    utime.sleep(0.7)
    

"""
Dieses Python-Skript ist für die Steuerung einer LED auf einem Mikrocontroller-Board wie dem
Raspberry Pi Pico vorgesehen. Das Skript verwendet die MicroPython-Bibliotheken machine
und utime, um die Steuerung der LED zu implementieren.

Zu Beginn wird der Benutzer aufgefordert, entweder "0" oder "1" einzugeben. Diese Eingabe
wird in der Variablen NullEins gespeichert.

Die folgende if-Anweisung prüft, ob der Benutzer "1" eingegeben hat. Wenn ja, versucht das
Skript, eine LED mit dem Namen "LED" zu initialisieren. Wenn diese LED nicht gefunden wird,
wird angenommen, dass es sich um einen Raspberry Pi Pico handelt, und der Pin 25 wird für
die LED-Initialisierung verwendet. Wenn die LED gefunden wird, wird davon ausgegangen,
dass es sich um ein Board handelt, das mit dem FeatherWing LED-Adapter von Adafruit
ausgestattet ist, und der Pin für die Initialisierung bleibt unverändert.

Wenn der Benutzer "0" eingegeben hat, wird die LED direkt mit dem Namen "LED" initialisiert,
ohne eine Fehlerprüfung durchzuführen.

Danach wird die LED mit einer Schleife in einer Endlosschleife ein- und ausgeschaltet, um
einen Blink-Effekt zu erzeugen. Die while-Schleife läuft ständig, bis das Programm
abgebrochen wird. Die LED_auf_Pico.value()-Funktion schaltet die LED ein und aus,
während die utime.sleep()-Funktion die Ausführung des Programms für eine bestimmte
Zeit anhält.















──────────────────────────────────────────────────────

>>> %Run -c $EDITOR_CONTENT

0 = ich probiere LED  und   1 = fehlertolerant: 1
ist Pico
blink - blink - blink - blink - blink

──────────────────────────────────────────────────────

>>> %Run -c $EDITOR_CONTENT

0 = ich probiere LED  und   1 = fehlertolerant: 0
Traceback (most recent call last):
  File "<stdin>", line 29, in <module>
TypeError: can't convert str to int
>>> 
Backend terminated or disconnected. Use 'Stop/Restart' to restart.

──────────────────────────────────────────────────────

>>> %Run -c $EDITOR_CONTENT

0 = ich probiere LED  und   1 = fehlertolerant: 1
ist Pico W
blink - blink - blink - blink - blink

──────────────────────────────────────────────────────

>>> %Run -c $EDITOR_CONTENT

0 = ich probiere LED  und   1 = fehlertolerant: 0
blink - blink - blink - blink - blink


"""
