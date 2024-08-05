#==========================================================================
#
# PB-01-1-60-bedingte Schleife.py
#
# (keine Bauteile)
#
#==========================================================================
#
Name = input("Wie heißt Du? ")

while Name != "Clark Kent":
    print("Du bist nicht Supermann  -  Versuchs nochmal!")
    Name = input("Wie heißt Du? ")
print("Du bist Supermann!")

"""
Das vorliegende MicroPython-Programm für den Raspberry Pi Pico beginnt damit,
den Benutzer nach seinem Namen zu fragen, indem die Funktion input() verwendet
wird. Die Benutzereingabe wird dann in der Variable Name gespeichert.

Die while-Schleife wird ausgeführt, solange der Wert von Name nicht gleich
Clark Kent ist. Innerhalb der Schleife wird eine Fehlermeldung ausgegeben,
die besagt, dass der Benutzer nicht Supermann ist, und der Benutzer wird
erneut nach seinem Namen gefragt. Die neue Eingabe wird dann erneut in die
Variable Name gespeichert.

Wenn der Wert von Name schließlich Clark Kent entspricht, wird die Schleife
beendet, und die Nachricht Du bist Supermann! wird ausgegeben.

Zusammenfassend fragt dieses Programm den Benutzer wiederholt nach seinem
Namen, bis er Clark Kent eingibt. Wenn dies der Fall ist, wird eine Nachricht
ausgegeben, die besagt, dass der Benutzer Supermann ist.

Nun zur verbalen Erklärung des Codes:

Das Programm beginnt mit der Eingabeaufforderung Wie heißt Du?, die mithilfe
der input()-Funktion ausgegeben wird. Der von dem Benutzer eingegebene Name
wird dann in der Variablen Name gespeichert.

Die while-Schleife wird ausgeführt, solange der Wert von Name nicht gleich
Clark Kent ist. Wenn die Bedingung erfüllt ist, wird die Fehlermeldung Du
bist nicht Supermann - Versuchs nochmal! ausgegeben, und der Benutzer wird
erneut nach seinem Namen gefragt. Die neue Eingabe wird dann erneut in der
Variable Name gespeichert.

Wenn der Benutzer schließlich Clark Kent eingibt und die Bedingung der
Schleife nicht mehr erfüllt ist, wird die Ausgabe Du bist Supermann! ausgegeben.

Dieses Programm ist ein gutes Beispiel für die Verwendung von Schleifen in
MicroPython, um eine Aktion zu wiederholen, bis eine bestimmte Bedingung
erfüllt ist. In diesem Fall wird die Bedingung erfüllt, wenn der Benutzer
seinen Namen als Clark Kent eingibt.


>>> %Run -c $EDITOR_CONTENT
Wie heißt Du? dieter
Du bist nicht Supermann  -  Versuchs nochmal!
Wie heißt Du? klaus
Du bist nicht Supermann  -  Versuchs nochmal!
Wie heißt Du? Clark Kent
Du bist Supermann!
>>>

"""