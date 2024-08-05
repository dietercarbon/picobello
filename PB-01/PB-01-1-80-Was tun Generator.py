#==========================================================================
#
# PB-01-1-80-Was tun Generator.py
#
# (keine Bauteile)
#
#==========================================================================
#
#Bibliotheken importieren
import random
import utime

wort1 = ["Ich gehe", "Wir gehen", "Oma geht", "Unsere Familie geht", "Papa geht"]
wort2 = ["heute", "morgen", "nächste Woche", "an Weihnachten", "an meinem Geburtstag", "übermorgen"]
wort3 = ["ins Schwimmbad.", "ins Kino.", "Pizza essen.", "in Urlaub.", "Ski fahren.", "in die Kirche."]

while True:
    zufall1 = random.randint(0,len(wort1)-1)
    zufall2 = random.randint(0,len(wort2)-1)
    zufall3 = random.randint(0,len(wort3)-1)

    print()
#    print(zufall1,zufall2,zufall3)
    print(wort1[zufall1],wort2[zufall2],wort3[zufall3])
    
    utime.sleep(2)
    
"""
Dieses MicroPython-Programm für den Raspberry Pi Pico generiert zufällige
Sätze, indem es jeweils ein zufälliges Wort aus drei verschiedenen Listen
auswählt.

Das Programm beginnt damit, die Module random und utime zu importieren.
random stellt Funktionen zum Generieren von Zufallszahlen bereit, während
utime Funktionen zur Zeitmessung und -verwaltung bietet.

Dann werden drei Listen mit verschiedenen Wörtern erstellt. Die Listen
wort1, wort2 und wort3 enthalten jeweils unterschiedliche Satzanfänge,
Zeitangaben und Aktivitäten.

In der while-Schleife werden dann drei Zufallszahlen mithilfe der
random.randint()-Funktion aus dem Modul random erzeugt, wobei die Länge
jeder Liste als oberer Grenzwert dient. Diese Zufallszahlen werden in den
Variablen zufall1, zufall2 und zufall3 gespeichert.

Mithilfe der print()-Funktion wird dann ein zufälliger Satz aus den drei
Listen zusammengesetzt und auf der Konsole ausgegeben. Die Wörter in jedem
Satz werden durch Kommas getrennt.

Das Programm pausiert dann für 2 Sekunden, bevor die Schleife erneut
durchlaufen wird.

Zusammenfassend generiert dieses Programm unendlich viele zufällige Sätze
aus den drei Listen, indem es jeweils ein zufälliges Wort aus jeder Liste
auswählt und zu einem Satz zusammensetzt. Jeder Satz wird alle 2 Sekunden
ausgegeben.

Nun zur verbalen Erklärung des Codes:

Das Programm importiert zuerst die Module random und utime. random wird
verwendet, um Zufallszahlen zu generieren, und utime wird zur Pausierung
des Programms verwendet.

Dann werden drei Listen wort1, wort2 und wort3 erstellt. Jede Liste enthält
eine Reihe von Wörtern, die jeweils einen Satzanfang, eine Zeitangabe und
eine Aktivität darstellen.

In der while-Schleife werden dann jeweils drei Zufallszahlen mithilfe der
random.randint()-Funktion aus dem Modul random generiert, die die Positionen
der zufällig ausgewählten Wörter in jeder Liste darstellen.

Mithilfe der print()-Funktion wird dann ein Satz zusammengesetzt, indem
jeweils ein zufälliges Wort aus jeder Liste ausgewählt wird. Die Wörter
werden durch Kommas getrennt und der Satz wird auf der Konsole ausgegeben.

Das Programm pausiert dann für 2 Sekunden mithilfe der Funktion
utime.sleep() und beginnt dann erneut mit der Generierung eines neuen
zufälligen Satzes.

Dieses Programm zeigt, wie Listen in MicroPython verwendet werden können,
um zufällige Sätze zu generieren, und wie das Modul random zur Erzeugung
von Zufallszahlen verwendet werden kann. Es ist auch ein gutes Beispiel
dafür, wie Pausen im Programm mit der utime.sleep()-Funktion eingelegt
werden können, um die Ausgabe zu verlangsamen.


>>> %Run -c $EDITOR_CONTENT

Wir gehen nächste Woche ins Schwimmbad.

Ich gehe an meinem Geburtstag Ski fahren.

Papa geht heute Pizza essen.

Ich gehe nächste Woche Ski fahren.

Oma geht morgen ins Kino.

Wir gehen an Weihnachten in Urlaub.

Papa geht an Weihnachten Pizza essen.



"""